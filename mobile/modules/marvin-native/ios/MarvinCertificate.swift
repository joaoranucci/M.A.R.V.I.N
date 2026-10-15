import CryptoKit
import Foundation
import Security

enum MarvinSecurityError: LocalizedError, Equatable {
  case invalidCertificate, invalidPin, invalidEndpoint, invalidRequest, cancelled, responseTooLarge

  var errorDescription: String? {
    switch self {
    case .invalidCertificate: return "Certificado do PC inválido, vencido ou incompatível com o endereço."
    case .invalidPin: return "A impressão digital do PC não confere com o pareamento."
    case .invalidEndpoint: return "O gateway requer um endereço HTTPS válido."
    case .invalidRequest: return "Requisição do gateway inválida."
    case .cancelled: return "Requisição cancelada."
    case .responseTooLarge: return "Resposta do gateway acima do limite."
    }
  }
}

/// Extract the complete DER SubjectPublicKeyInfo, not SecKey's raw EC point.
/// This is exactly the SHA-256 SPKI contract used by cryptography/OkHttp on the PC/Android.
enum MarvinCertificate {
  private struct Node {
    let tag: UInt8
    let start: Int
    let content: Int
    let end: Int
  }

  private static func node(_ bytes: [UInt8], _ offset: Int, limit: Int) throws -> Node {
    guard offset >= 0, offset + 2 <= limit, limit <= bytes.count else { throw MarvinSecurityError.invalidCertificate }
    var cursor = offset + 1
    let first = bytes[cursor]
    cursor += 1
    var count = Int(first)
    if first & 0x80 != 0 {
      let length = Int(first & 0x7f)
      guard length > 0, length <= 4, cursor + length <= limit, bytes[cursor] != 0 else {
        throw MarvinSecurityError.invalidCertificate
      }
      count = 0
      for _ in 0..<length { count = (count << 8) | Int(bytes[cursor]); cursor += 1 }
      guard count >= 128 else { throw MarvinSecurityError.invalidCertificate }
    }
    guard count <= limit - cursor else { throw MarvinSecurityError.invalidCertificate }
    return Node(tag: bytes[offset], start: offset, content: cursor, end: cursor + count)
  }

  private static func children(_ bytes: [UInt8], _ parent: Node) throws -> [Node] {
    var result: [Node] = []
    var cursor = parent.content
    while cursor < parent.end {
      guard result.count < 32 else { throw MarvinSecurityError.invalidCertificate }
      let next = try node(bytes, cursor, limit: parent.end)
      result.append(next)
      cursor = next.end
    }
    return result
  }

  private static func fields(_ certificate: SecCertificate) throws -> ([UInt8], [Node]) {
    let bytes = [UInt8](SecCertificateCopyData(certificate) as Data)
    guard bytes.count <= 65536 else { throw MarvinSecurityError.invalidCertificate }
    let root = try node(bytes, 0, limit: bytes.count)
    guard root.tag == 0x30, root.end == bytes.count else { throw MarvinSecurityError.invalidCertificate }
    let outer = try children(bytes, root)
    guard outer.count == 3, outer[0].tag == 0x30 else { throw MarvinSecurityError.invalidCertificate }
    var tbs = try children(bytes, outer[0])
    if tbs.first?.tag == 0xa0 { tbs.removeFirst() }
    guard tbs.count >= 6, tbs[3].tag == 0x30, tbs[5].tag == 0x30 else {
      throw MarvinSecurityError.invalidCertificate
    }
    return (bytes, tbs)
  }

  static func pin(_ certificate: SecCertificate) throws -> String {
    let (bytes, tbs) = try fields(certificate)
    let spki = tbs[5]
    return Data(SHA256.hash(data: Data(bytes[spki.start..<spki.end]))).base64EncodedString()
  }

  private static func date(_ bytes: [UInt8], _ node: Node) throws -> Date {
    guard let text = String(bytes: bytes[node.content..<node.end], encoding: .ascii) else {
      throw MarvinSecurityError.invalidCertificate
    }
    let expanded: String
    if node.tag == 0x17, text.count == 13, let year = Int(text.prefix(2)) {
      expanded = (year >= 50 ? "19" : "20") + text
    } else if node.tag == 0x18, text.count == 15 {
      expanded = text
    } else { throw MarvinSecurityError.invalidCertificate }
    guard expanded.last == "Z", expanded.dropLast().allSatisfy({ $0.isASCII && $0.isNumber }) else {
      throw MarvinSecurityError.invalidCertificate
    }
    let parser = DateFormatter()
    parser.locale = Locale(identifier: "en_US_POSIX")
    parser.calendar = Calendar(identifier: .gregorian)
    parser.timeZone = TimeZone(secondsFromGMT: 0)
    parser.dateFormat = "yyyyMMddHHmmss'Z'"
    parser.isLenient = false
    guard let result = parser.date(from: expanded), parser.string(from: result) == expanded else {
      throw MarvinSecurityError.invalidCertificate
    }
    return result
  }

  static func validity(_ certificate: SecCertificate) throws -> (Date, Date) {
    let (bytes, tbs) = try fields(certificate)
    let dates = try children(bytes, tbs[3])
    guard dates.count == 2 else { throw MarvinSecurityError.invalidCertificate }
    return (try date(bytes, dates[0]), try date(bytes, dates[1]))
  }

  static func samePin(_ lhs: String, _ rhs: String) -> Bool {
    guard let left = Data(base64Encoded: lhs), let right = Data(base64Encoded: rhs),
          left.count == 32, right.count == 32 else { return false }
    var difference: UInt8 = 0
    for (a, b) in zip(left, right) { difference |= a ^ b }
    return difference == 0
  }

  @discardableResult
  static func validate(_ trust: SecTrust, host: String, expectedPin: String?, now: Date = Date()) throws -> SecCertificate {
    guard let chain = SecTrustCopyCertificateChain(trust) as? [SecCertificate], let leaf = chain.first else {
      throw MarvinSecurityError.invalidCertificate
    }
    if let expectedPin, !samePin(try pin(leaf), expectedPin) { throw MarvinSecurityError.invalidPin }
    let (start, end) = try validity(leaf)
    guard start <= now, now <= end else { throw MarvinSecurityError.invalidCertificate }
    // Trust is scoped to this one challenge. No global trust override and no hostname bypass.
    // A custom anchor is necessary for the gateway's self-signed certificate; the pin was checked first.
    guard SecTrustSetPolicies(trust, SecPolicyCreateSSL(true, host as CFString)) == errSecSuccess,
          SecTrustSetAnchorCertificates(trust, [leaf] as CFArray) == errSecSuccess,
          SecTrustSetAnchorCertificatesOnly(trust, true) == errSecSuccess,
          SecTrustSetVerifyDate(trust, now as CFDate) == errSecSuccess,
          SecTrustSetNetworkFetchAllowed(trust, false) == errSecSuccess else { throw MarvinSecurityError.invalidCertificate }
    var trustError: CFError?
    guard SecTrustEvaluateWithError(trust, &trustError) else {
      throw MarvinSecurityError.invalidCertificate
    }
    return leaf
  }
}
