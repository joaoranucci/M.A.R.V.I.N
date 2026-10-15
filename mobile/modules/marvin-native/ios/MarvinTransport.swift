import Foundation
import Security

typealias MarvinHTTPCompletion = (Result<[String: Any], Error>) -> Void

/// Each operation has its own ephemeral session, fixed host and expected pin.
/// A valid public CA certificate never bypasses a gateway pin.
final class MarvinTransport {
  private let queue = DispatchQueue(label: "dev.marvin.http")
  private var pins: Set<String> = []
  private var operations: [String: MarvinRequest] = [:]
  private var cancelled: Set<String> = []
  private var closed = false

  func setPins(_ values: [String]) {
    queue.sync {
      pins = Set(values.filter { Data(base64Encoded: $0)?.count == 32 })
      for operation in operations.values where operation.pin.map({ !pins.contains($0) }) ?? false {
        operation.cancel()
      }
    }
  }

  func getPins() -> [String] { queue.sync { Array(pins) } }

  func request(_ options: [String: Any], completion: @escaping MarvinHTTPCompletion) {
    queue.async { self.begin(options, probe: false, completion: completion) }
  }

  func probe(host: String, port: Int, completion: @escaping MarvinHTTPCompletion) {
    var address = URLComponents()
    address.scheme = "https"
    address.host = host
    address.port = port
    address.path = "/v1/health"
    guard (1...65535).contains(port), let url = address.url else {
      completion(.failure(MarvinSecurityError.invalidEndpoint)); return
    }
    let options: [String: Any] = ["id": UUID().uuidString, "url": url.absoluteString, "method": "GET", "timeoutMs": 6000]
    queue.async { self.begin(options, probe: true, completion: completion) }
  }

  private func begin(_ options: [String: Any], probe: Bool, completion: @escaping MarvinHTTPCompletion) {
    guard let id = options["id"] as? String, !id.isEmpty, id.count <= 100, !closed, operations[id] == nil else {
      completion(.failure(MarvinSecurityError.invalidRequest)); return
    }
    if cancelled.remove(id) != nil { completion(.failure(MarvinSecurityError.cancelled)); return }
    let pin = options["pin"] as? String
    if !probe && (pin == nil || !pins.contains(pin!)) { completion(.failure(MarvinSecurityError.invalidPin)); return }
    do {
      let operation = try MarvinRequest(options, pin: pin, probe: probe) { [weak self] result in
        self?.queue.async { self?.operations.removeValue(forKey: id) }
        completion(result)
      }
      operations[id] = operation
      do { try operation.start() } catch { operation.fail(error) }
    } catch { completion(.failure(error)) }
  }

  func cancel(_ id: String) {
    queue.async {
      if let operation = self.operations[id] { operation.cancel() }
      else {
        if self.cancelled.count >= 1024 { self.cancelled.removeAll() }
        self.cancelled.insert(id)
      }
    }
  }

  func close() {
    queue.async {
      self.closed = true
      for operation in self.operations.values { operation.cancel() }
      self.operations.removeAll()
      self.pins.removeAll()
      self.cancelled.removeAll()
    }
  }
}

private final class MarvinRequest: NSObject, URLSessionDataDelegate, URLSessionTaskDelegate {
  let pin: String?
  private let options: [String: Any]
  private let url: URL
  private let host: String
  private let probe: Bool
  private let binary: Bool
  private let completion: MarvinHTTPCompletion
  private var session: URLSession?
  private var task: URLSessionTask?
  private var uploadFile: URL?
  private var body = Data()
  private var status = 0
  private let lock = NSLock()
  private var completed = false
  private let maxResponse = 32 * 1024 * 1024

  init(_ options: [String: Any], pin: String?, probe: Bool, completion: @escaping MarvinHTTPCompletion) throws {
    guard let raw = options["url"] as? String, raw.count < 16384,
          let url = URL(string: raw), let parts = URLComponents(url: url, resolvingAgainstBaseURL: false),
          parts.scheme == "https", let host = parts.host, !host.isEmpty,
          parts.user == nil, parts.password == nil, parts.fragment == nil,
          (1...65535).contains(parts.port ?? 443), url.path.hasPrefix("/v1/") else {
      throw MarvinSecurityError.invalidEndpoint
    }
    self.url = url
    self.host = host.hasPrefix("[") && host.hasSuffix("]") ? String(host.dropFirst().dropLast()) : host
    self.options = options
    self.pin = pin
    self.probe = probe
    self.binary = options["binary"] as? Bool ?? false
    self.completion = completion
    super.init()
  }

  func start() throws {
    let milliseconds = (options["timeoutMs"] as? NSNumber)?.doubleValue ?? 15000
    let timeout = max(1, min(300, milliseconds / 1000))
    var request = URLRequest(url: url, cachePolicy: .reloadIgnoringLocalAndRemoteCacheData, timeoutInterval: timeout)
    let method = options["method"] as? String ?? "GET"
    guard ["GET", "POST", "PUT", "DELETE"].contains(method) else { throw MarvinSecurityError.invalidRequest }
    request.httpMethod = method
    if let headers = options["headers"] as? [String: String] {
      guard headers.count <= 32 else { throw MarvinSecurityError.invalidRequest }
      for (key, value) in headers {
        guard key.range(of: "^[A-Za-z0-9-]+$", options: .regularExpression) != nil,
              !["host", "cookie", "connection", "content-length", "proxy-authorization"].contains(key.lowercased()),
              value.count <= 8192, !value.unicodeScalars.contains(where: { $0.value < 32 || $0.value == 127 }) else {
          throw MarvinSecurityError.invalidRequest
        }
        request.setValue(value, forHTTPHeaderField: key)
      }
    }
    if let upload = options["upload"] as? [String: Any] {
      guard method == "POST", options["body"] == nil else { throw MarvinSecurityError.invalidRequest }
      let boundary = "marvin-" + UUID().uuidString
      uploadFile = try multipart(upload, boundary: boundary)
      request.setValue("multipart/form-data; boundary=" + boundary, forHTTPHeaderField: "Content-Type")
    } else if let text = options["body"] as? String {
      guard text.utf8.count <= 256 * 1024, method != "GET" else { throw MarvinSecurityError.invalidRequest }
      request.httpBody = Data(text.utf8)
    }
    let configuration = URLSessionConfiguration.ephemeral
    configuration.urlCache = nil
    configuration.urlCredentialStorage = nil
    configuration.httpCookieStorage = nil
    configuration.httpShouldSetCookies = false
    configuration.requestCachePolicy = .reloadIgnoringLocalAndRemoteCacheData
    configuration.timeoutIntervalForRequest = timeout
    configuration.timeoutIntervalForResource = timeout
    configuration.tlsMinimumSupportedProtocolVersion = .TLSv12
    let delegateQueue = OperationQueue()
    delegateQueue.maxConcurrentOperationCount = 1
    let created = URLSession(configuration: configuration, delegate: self, delegateQueue: delegateQueue)
    session = created
    if let uploadFile { task = created.uploadTask(with: request, fromFile: uploadFile) }
    else { task = created.dataTask(with: request) }
    task?.resume()
  }

  func cancel() { fail(MarvinSecurityError.cancelled) }
  func fail(_ error: Error) { finish(.failure(error)) }

  private func finish(_ result: Result<[String: Any], Error>) {
    lock.lock()
    if completed { lock.unlock(); return }
    completed = true
    lock.unlock()
    session?.invalidateAndCancel()
    if let uploadFile { try? FileManager.default.removeItem(at: uploadFile) }
    completion(result)
  }

  private var isCompleted: Bool {
    lock.lock(); defer { lock.unlock() }
    return completed
  }

  private func challenge(_ challenge: URLAuthenticationChallenge,
                         completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
    guard !isCompleted, challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodServerTrust,
          challenge.protectionSpace.host.lowercased() == host.lowercased(),
          let trust = challenge.protectionSpace.serverTrust else {
      completionHandler(.cancelAuthenticationChallenge, nil)
      fail(MarvinSecurityError.invalidCertificate)
      return
    }
    do {
      let leaf = try MarvinCertificate.validate(trust, host: host, expectedPin: pin)
      if probe {
        let (_, expires) = try MarvinCertificate.validity(leaf)
        let subject = SecCertificateCopySubjectSummary(leaf) as String? ?? "MARVIN Gateway"
        completionHandler(.cancelAuthenticationChallenge, nil)
        // Inspection sends no HTTP request, pairing code or device token.
        finish(.success(["pin": try MarvinCertificate.pin(leaf), "subject": subject, "notAfter": expires.timeIntervalSince1970 * 1000]))
      } else {
        completionHandler(.useCredential, URLCredential(trust: trust))
      }
    } catch {
      completionHandler(.cancelAuthenticationChallenge, nil)
      fail(error)
    }
  }

  func urlSession(_ session: URLSession, didReceive challenge: URLAuthenticationChallenge,
                  completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
    self.challenge(challenge, completionHandler: completionHandler)
  }

  func urlSession(_ session: URLSession, task: URLSessionTask, didReceive challenge: URLAuthenticationChallenge,
                  completionHandler: @escaping (URLSession.AuthChallengeDisposition, URLCredential?) -> Void) {
    self.challenge(challenge, completionHandler: completionHandler)
  }

  func urlSession(_ session: URLSession, task: URLSessionTask, willPerformHTTPRedirection response: HTTPURLResponse,
                  newRequest request: URLRequest, completionHandler: @escaping (URLRequest?) -> Void) {
    completionHandler(nil) // Credentials never follow redirects, even to another paired PC.
  }

  func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive response: URLResponse,
                  completionHandler: @escaping (URLSession.ResponseDisposition) -> Void) {
    guard !probe, !isCompleted, let http = response as? HTTPURLResponse else {
      completionHandler(.cancel); fail(MarvinSecurityError.invalidCertificate); return
    }
    guard response.expectedContentLength <= Int64(maxResponse) else {
      completionHandler(.cancel); fail(MarvinSecurityError.responseTooLarge); return
    }
    status = http.statusCode
    completionHandler(.allow)
  }

  func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive data: Data) {
    guard !isCompleted else { return }
    guard body.count <= maxResponse - data.count else { fail(MarvinSecurityError.responseTooLarge); return }
    body.append(data)
  }

  func urlSession(_ session: URLSession, task: URLSessionTask, didCompleteWithError error: Error?) {
    guard !isCompleted else { return }
    if let error { fail(error); return }
    guard status > 0 else { fail(MarvinSecurityError.invalidCertificate); return }
    let text: String
    if binary && (200..<300).contains(status) { text = body.base64EncodedString() }
    else {
      guard let decoded = String(data: body, encoding: .utf8) else { fail(MarvinSecurityError.invalidRequest); return }
      text = decoded
    }
    finish(.success(["status": status, "body": text, "binary": binary && (200..<300).contains(status)]))
  }

  private func multipart(_ upload: [String: Any], boundary: String) throws -> URL {
    guard let file = upload["file"] as? [String: String], let uri = file["uri"], let url = URL(string: uri), url.isFileURL,
          let fields = upload["fields"] as? [String: String], Set(fields.keys) == Set(["client_id", "category"]) else {
      throw MarvinSecurityError.invalidRequest
    }
    let source = url.resolvingSymlinksInPath().standardizedFileURL
    let roots = [FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first,
                 FileManager.default.urls(for: .cachesDirectory, in: .userDomainMask).first,
                 FileManager.default.temporaryDirectory].compactMap { $0?.resolvingSymlinksInPath().standardizedFileURL }
    guard roots.contains(where: { source.path.hasPrefix($0.path + "/") }) else { throw MarvinSecurityError.invalidRequest }
    let values = try source.resourceValues(forKeys: [.isRegularFileKey, .fileSizeKey])
    guard values.isRegularFile == true, let size = values.fileSize, size > 0, size <= 20 * 1024 * 1024 else {
      throw MarvinSecurityError.invalidRequest
    }
    let target = FileManager.default.temporaryDirectory.appendingPathComponent("marvin-upload-" + UUID().uuidString)
    guard FileManager.default.createFile(atPath: target.path, contents: nil) else { throw MarvinSecurityError.invalidRequest }
    do {
      #if os(iOS)
      try FileManager.default.setAttributes([.protectionKey: FileProtectionType.complete], ofItemAtPath: target.path)
      #endif
      let output = try FileHandle(forWritingTo: target)
      defer { try? output.close() }
      func write(_ text: String) throws { try output.write(contentsOf: Data(text.utf8)) }
      for key in ["client_id", "category"] {
        let value = fields[key]!
        guard value.utf8.count <= 1024 else { throw MarvinSecurityError.invalidRequest }
        try write("--" + boundary + "\r\nContent-Disposition: form-data; name=\"" + key + "\"\r\n\r\n" + value + "\r\n")
      }
      let name = String((file["name"] ?? "documento").prefix(160)).replacingOccurrences(of: "[\\r\\n\"/\\\\]", with: "_", options: .regularExpression)
      let mime = file["mimeType"] ?? "application/octet-stream"
      let safeMime = mime.range(of: "^[A-Za-z0-9.+-]+/[A-Za-z0-9.+-]+$", options: .regularExpression) == nil ? "application/octet-stream" : mime
      try write("--" + boundary + "\r\nContent-Disposition: form-data; name=\"file\"; filename=\"" + name + "\"\r\nContent-Type: " + safeMime + "\r\n\r\n")
      let input = try FileHandle(forReadingFrom: source)
      defer { try? input.close() }
      var copied = 0
      while let data = try input.read(upToCount: 65536), !data.isEmpty {
        copied += data.count
        guard copied <= size else { throw MarvinSecurityError.invalidRequest }
        try output.write(contentsOf: data)
      }
      guard copied == size else { throw MarvinSecurityError.invalidRequest }
      try write("\r\n--" + boundary + "--\r\n")
      return target
    } catch {
      try? FileManager.default.removeItem(at: target)
      throw error
    }
  }
}
