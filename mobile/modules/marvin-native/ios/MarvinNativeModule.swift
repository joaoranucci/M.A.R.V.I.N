import ExpoModulesCore

public class MarvinNativeModule: Module {
  private let transport = MarvinTransport()
  private lazy var audio = MarvinAudioSession { [weak self] name, body in self?.sendEvent(name, body) }

  private func settle(_ result: Result<[String: Any], Error>, promise: Promise) {
    switch result {
    case .success(let value): promise.resolve(value)
    case .failure(let error):
      let code = (error as? MarvinSecurityError) == .cancelled ? "E_ABORTED" : "E_SECURE_TRANSPORT"
      promise.reject(code, error.localizedDescription)
    }
  }

  public func definition() -> ModuleDefinition {
    Name("MarvinNative")
    Events("onAudioFocusChange", "onAudioRouteChange", "onBecomingNoisy", "onCallStateChange", "onSharedFiles")
    OnCreate { self.audio.start() }
    OnDestroy { self.audio.stop(); self.transport.close() }

    Function("getTransportCapabilities") { ["http": "urlsession-pinned-v1"] }
    Function("setPinnedKeys") { (pins: [String]) in self.transport.setPins(pins) }
    Function("getPinnedKeys") { self.transport.getPins() }
    AsyncFunction("gatewayRequest") { (options: [String: Any], promise: Promise) in
      self.transport.request(options) { result in self.settle(result, promise: promise) }
    }
    Function("cancelRequest") { (id: String) in self.transport.cancel(id) }
    AsyncFunction("probeCertificate") { (host: String, port: Int, promise: Promise) in
      self.transport.probe(host: host, port: port) { result in self.settle(result, promise: promise) }
    }

    Function("requestAudioFocus") { (kind: String) in self.audio.request(kind) }
    Function("abandonAudioFocus") { self.audio.abandon() }
    Function("getAudioState") { self.audio.state() }
    Function("setPreferredAudioRoute") { (route: String) in self.audio.setRoute(route) }

    // Document import uses the system picker. A Share Extension is a separate app target, not a stubbed feature.
    Function("consumeSharedFiles") { () -> [String: Any]? in nil }
  }
}
