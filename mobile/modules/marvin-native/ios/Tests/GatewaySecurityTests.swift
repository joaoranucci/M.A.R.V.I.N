import Foundation
import Security
import XCTest
@testable import MarvinGatewaySecurity

final class GatewaySecurityTests: XCTestCase {
  private var fixtures: [String: [String: Any]] = [:]
  private var directory: URL!
  private var transport: MarvinTransport!

  override func setUpWithError() throws {
    guard let root = ProcessInfo.processInfo.environment["MARVIN_CERT_FIXTURES"] else {
      throw XCTSkip("Run scripts/ios_tls_fixtures.py --serve and set MARVIN_CERT_FIXTURES.")
    }
    directory = URL(fileURLWithPath: root)
    fixtures = try JSONSerialization.jsonObject(with: Data(contentsOf: directory.appendingPathComponent("fixtures.json"))) as! [String: [String: Any]]
    transport = MarvinTransport()
    transport.setPins(fixtures.values.compactMap { $0["pin"] as? String })
  }

  override func tearDown() { transport?.close() }

  private func cert(_ name: String) throws -> SecCertificate {
    let data = try Data(contentsOf: directory.appendingPathComponent(name + ".der"))
    return try XCTUnwrap(SecCertificateCreateWithData(nil, data as CFData))
  }

  private func trust(_ name: String) throws -> SecTrust {
    var result: SecTrust?
    XCTAssertEqual(SecTrustCreateWithCertificates(try cert(name), SecPolicyCreateSSL(true, "127.0.0.1" as CFString), &result), errSecSuccess)
    return try XCTUnwrap(result)
  }

  private func request(_ name: String = "valid", path: String = "/v1/health",
                       extra: [String: Any] = [:]) throws -> [String: Any] {
    var options: [String: Any] = [
      "id": UUID().uuidString, "url": "https://127.0.0.1:\(fixtures[name]!["port"]! )" + path,
      "pin": fixtures[name]!["pin"]!, "method": "GET", "timeoutMs": 4000,
      "headers": ["Authorization": "Bearer unit-test"]
    ]
    for (key, value) in extra { options[key] = value }
    let finished = expectation(description: "HTTPS operation")
    var received: Result<[String: Any], Error>?
    transport.request(options) { received = $0; finished.fulfill() }
    wait(for: [finished], timeout: 8)
    return try XCTUnwrap(received).get()
  }

  func testSPKIExactlyMatchesPythonGatewayForECAndRSA() throws {
    for name in ["valid", "rsa"] {
      XCTAssertEqual(try MarvinCertificate.pin(cert(name)), fixtures[name]!["pin"] as? String)
    }
  }

  func testCertificateDatesAndHostnameAreValidatedEvenWhenPinned() throws {
    XCTAssertNoThrow(try MarvinCertificate.validate(trust("valid"), host: "127.0.0.1", expectedPin: fixtures["valid"]!["pin"] as? String))
    for name in ["expired", "future", "wrong-host"] {
      XCTAssertThrowsError(try MarvinCertificate.validate(trust(name), host: "127.0.0.1", expectedPin: fixtures[name]!["pin"] as? String), name)
    }
    XCTAssertThrowsError(try MarvinCertificate.validate(trust("valid"), host: "another-pc.invalid", expectedPin: fixtures["valid"]!["pin"] as? String))
  }

  func testPinnedHTTPSAndLongPollingUseTheSameTransport() throws {
    XCTAssertEqual(try request()["status"] as? Int, 200)
    let events = try request(path: "/v1/events?after=0&wait=1")
    XCTAssertEqual(events["status"] as? Int, 200)
    XCTAssertTrue((events["body"] as? String)?.contains("last_seq") == true)
  }

  func testUnpinnedCertificateSendsNoHTTPOrAuthorization() throws {
    let before = try request(path: "/v1/count")["body"] as! String
    let wrongPin = Data(repeating: 0, count: 32).base64EncodedString()
    transport.setPins([fixtures["valid"]!["pin"] as! String, wrongPin])
    XCTAssertThrowsError(try request(extra: ["pin": wrongPin]))
    XCTAssertEqual(try request(path: "/v1/count")["body"] as? String, before)
  }

  func testExpiredFutureAndWrongHostAreRejectedByRealTLS() {
    for name in ["expired", "future", "wrong-host"] { XCTAssertThrowsError(try request(name), name) }
  }

  func testProbeIsInspectionOnlyAndNeverSendsAnHTTPRequest() throws {
    let before = try request(path: "/v1/count")["body"] as! String
    let finished = expectation(description: "probe")
    var result: Result<[String: Any], Error>?
    transport.probe(host: "127.0.0.1", port: fixtures["valid"]!["port"] as! Int) { result = $0; finished.fulfill() }
    wait(for: [finished], timeout: 8)
    XCTAssertEqual(try XCTUnwrap(result).get()["pin"] as? String, fixtures["valid"]!["pin"] as? String)
    XCTAssertEqual(try request(path: "/v1/count")["body"] as? String, before)
  }

  func testRedirectsAreReturnedWithoutFollowingOrForwardingCredentials() throws {
    XCTAssertEqual(try request(path: "/v1/redirect")["status"] as? Int, 302)
  }

  func testBinaryAudioRoundTripsExactly() throws {
    let response = try request(path: "/v1/binary", extra: ["binary": true])
    XCTAssertEqual(response["binary"] as? Bool, true)
    XCTAssertEqual(Data(base64Encoded: response["body"] as! String), Data((0...255).map { UInt8($0) }))
  }

  func testDocumentMultipartAndSandboxBoundary() throws {
    let file = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString + ".md")
    try Data("# documento em português".utf8).write(to: file)
    defer { try? FileManager.default.removeItem(at: file) }
    var upload: [String: Any] = ["file": ["uri": file.absoluteString, "name": "teste.md", "mimeType": "text/markdown"],
                               "fields": ["client_id": "document-test", "category": "pessoal"]]
    let response = try request(path: "/v1/documents", extra: ["method": "POST", "upload": upload])
    XCTAssertEqual(response["status"] as? Int, 201)
    XCTAssertTrue((response["body"] as? String)?.contains("multipart_ok") == true)
    upload["file"] = ["uri": "file:///etc/hosts", "name": "hosts", "mimeType": "text/plain"]
    XCTAssertThrowsError(try request(path: "/v1/documents", extra: ["method": "POST", "upload": upload]))
  }

  func testCancellationBeforeDispatchAndDuringLongPoll() throws {
    let id = "already-cancelled"
    transport.cancel(id)
    XCTAssertThrowsError(try request(extra: ["id": id]))
    let activeID = UUID().uuidString
    DispatchQueue.global().asyncAfter(deadline: .now() + 0.1) { self.transport.cancel(activeID) }
    XCTAssertThrowsError(try request(path: "/v1/slow", extra: ["id": activeID]))
  }
}
