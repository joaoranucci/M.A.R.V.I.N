import AVFoundation
import Foundation

/// Shared with STT, expo-speech (application audio session) and expo-audio.
/// Interruptions stop capture/playback in JS; they never automatically resume a conversation.
final class MarvinAudioSession {
  private let queue = DispatchQueue(label: "dev.marvin.audio")
  private let session = AVAudioSession.sharedInstance()
  private let emit: (String, [String: Any]) -> Void
  private var observers: [NSObjectProtocol] = []
  private var interrupted = false
  private var active = false
  private var kind = "speak"
  private var preferred = "system"

  init(emit: @escaping (String, [String: Any]) -> Void) { self.emit = emit }

  func start() {
    queue.sync {
      guard observers.isEmpty else { return }
      let center = NotificationCenter.default
      observers.append(center.addObserver(forName: AVAudioSession.interruptionNotification, object: session, queue: nil) { [weak self] note in
        self?.queue.async { self?.interruption(note) }
      })
      observers.append(center.addObserver(forName: AVAudioSession.routeChangeNotification, object: session, queue: nil) { [weak self] note in
        self?.queue.async { self?.routeChange(note) }
      })
      observers.append(center.addObserver(forName: AVAudioSession.mediaServicesWereResetNotification, object: session, queue: nil) { [weak self] _ in
        self?.queue.async {
          guard let self else { return }
          self.active = false
          self.emitFocus("loss")
        }
      })
    }
  }

  func stop() {
    queue.sync {
      for observer in observers { NotificationCenter.default.removeObserver(observer) }
      observers.removeAll()
      deactivate()
    }
  }

  private func configure() throws {
    var options: AVAudioSession.CategoryOptions = [.allowBluetooth, .allowBluetoothA2DP, .allowAirPlay]
    if preferred != "earpiece" { options.insert(.defaultToSpeaker) }
    try session.setCategory(.playAndRecord, mode: kind == "listen" ? .measurement : .default, options: options)
    try session.setActive(true)
    try session.overrideOutputAudioPort(preferred == "speaker" ? .speaker : .none)
    active = true
  }

  func request(_ value: String) -> Bool {
    queue.sync {
      guard ["speak", "listen"].contains(value), !interrupted else { return false }
      kind = value
      do { try configure(); return true }
      catch { active = false; return false }
    }
  }

  func abandon() { queue.sync { deactivate() } }

  private func deactivate() {
    if active { try? session.setActive(false, options: .notifyOthersOnDeactivation) }
    active = false
  }

  func setRoute(_ value: String) -> Bool {
    queue.sync {
      guard ["system", "speaker", "earpiece"].contains(value) else { return false }
      let previous = preferred
      preferred = value
      do {
        if active { try configure() }
        emit("onAudioRouteChange", snapshot())
        return true
      } catch { preferred = previous; return false }
    }
  }

  func state() -> [String: Any] { queue.sync { snapshot() } }

  private func route(_ port: AVAudioSession.Port) -> String {
    switch port {
    case .builtInReceiver: return "earpiece"
    case .headphones, .lineOut: return "wired"
    case .bluetoothA2DP, .bluetoothHFP, .bluetoothLE: return "bluetooth"
    case .usbAudio: return "usb"
    case .HDMI: return "hdmi"
    case .airPlay: return "airplay"
    default: return "speaker"
    }
  }

  private func snapshot() -> [String: Any] {
    let outputs = session.currentRoute.outputs.map { route($0.portType) }
    return ["outputs": outputs, "route": outputs.first ?? "speaker",
            "mode": active ? (kind == "listen" ? 1 : 2) : 0,
            // iOS does not identify arbitrary phone calls here: this is a conservative system-interruption flag.
            "inCall": interrupted, "volume": Double(session.outputVolume), "maxVolume": 1]
  }

  private func emitFocus(_ change: String) {
    var event = snapshot()
    event["change"] = change
    event["kind"] = kind
    emit("onAudioFocusChange", event)
  }

  private func interruption(_ note: Notification) {
    guard let raw = (note.userInfo?[AVAudioSessionInterruptionTypeKey] as? NSNumber)?.uintValue,
          let type = AVAudioSession.InterruptionType(rawValue: raw) else { return }
    interrupted = type == .began
    if interrupted { active = false }
    emit("onCallStateChange", snapshot())
    emitFocus(interrupted ? "loss_transient" : "gain")
    // Ignore shouldResume: the user must tap again after a call/system interruption.
  }

  private func routeChange(_ note: Notification) {
    let raw = (note.userInfo?[AVAudioSessionRouteChangeReasonKey] as? NSNumber)?.uintValue ?? 0
    if AVAudioSession.RouteChangeReason(rawValue: raw) == .oldDeviceUnavailable {
      deactivate()
      emit("onBecomingNoisy", snapshot())
    }
    emit("onAudioRouteChange", snapshot())
  }
}
