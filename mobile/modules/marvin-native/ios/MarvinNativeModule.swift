import ExpoModulesCore

// iOS is not implemented in v0.1. These stubs keep the JS API stable;
// certificate pinning, audio session and share extension need their own work on iOS.
public class MarvinNativeModule: Module {
  public func definition() -> ModuleDefinition {
    Name("MarvinNative")
    Events("onAudioFocusChange", "onAudioRouteChange", "onBecomingNoisy", "onCallStateChange", "onSharedFiles")
    Function("setPinnedKeys") { (_: [String]) in }
    Function("getPinnedKeys") { () -> [String] in [] }
    AsyncFunction("probeCertificate") { (_: String, _: Int) -> [String: Any?] in
      throw Exception(name: "Unsupported", description: "Pareamento manual ainda não implementado no iOS.")
    }
    Function("requestAudioFocus") { (_: String) -> Bool in true }
    Function("abandonAudioFocus") {}
    Function("getAudioState") { () -> [String: Any?] in
      ["outputs": [], "route": "speaker", "mode": 0, "inCall": false, "volume": 0, "maxVolume": 0]
    }
    Function("consumeSharedFiles") { () -> [String: Any?]? in nil }
  }
}
