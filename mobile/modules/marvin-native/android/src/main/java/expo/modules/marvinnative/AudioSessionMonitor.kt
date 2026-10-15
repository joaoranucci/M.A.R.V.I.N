package expo.modules.marvinnative

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.media.AudioAttributes
import android.media.AudioDeviceCallback
import android.media.AudioDeviceInfo
import android.media.AudioFocusRequest
import android.media.AudioManager
import android.os.Build
import android.os.Handler
import android.os.Looper
import androidx.core.content.ContextCompat

/**
 * Audio focus, output routes, headphone disconnection and call state.
 *
 * Speech output and recognition both go through this single focus owner, so a
 * phone call or another app taking focus reaches JS as one event.
 */
class AudioSessionMonitor(
  private val context: Context,
  private val emit: (String, Map<String, Any?>) -> Unit
) {
  private val audio = context.getSystemService(Context.AUDIO_SERVICE) as AudioManager
  private val handler = Handler(Looper.getMainLooper())
  private var request: AudioFocusRequest? = null
  private var generation = 0
  private var started = false

  private val deviceCallback = object : AudioDeviceCallback() {
    override fun onAudioDevicesAdded(addedDevices: Array<out AudioDeviceInfo>) = emit("onAudioRouteChange", state())
    override fun onAudioDevicesRemoved(removedDevices: Array<out AudioDeviceInfo>) = emit("onAudioRouteChange", state())
  }

  private val noisyReceiver = object : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
      if (intent.action == AudioManager.ACTION_AUDIO_BECOMING_NOISY) emit("onBecomingNoisy", state())
    }
  }

  private val modeListener: Any? =
    if (Build.VERSION.SDK_INT >= 31) AudioManager.OnModeChangedListener { emit("onCallStateChange", state()) } else null

  fun start() {
    if (started) return
    started = true
    audio.registerAudioDeviceCallback(deviceCallback, handler)
    ContextCompat.registerReceiver(context, noisyReceiver, IntentFilter(AudioManager.ACTION_AUDIO_BECOMING_NOISY),
      ContextCompat.RECEIVER_NOT_EXPORTED)
    if (Build.VERSION.SDK_INT >= 31) {
      audio.addOnModeChangedListener(ContextCompat.getMainExecutor(context), modeListener as AudioManager.OnModeChangedListener)
    }
  }

  fun stop() {
    if (!started) return
    started = false
    abandon()
    audio.unregisterAudioDeviceCallback(deviceCallback)
    try {
      context.unregisterReceiver(noisyReceiver)
    } catch (_: IllegalArgumentException) {
    }
    if (Build.VERSION.SDK_INT >= 31) {
      audio.removeOnModeChangedListener(modeListener as AudioManager.OnModeChangedListener)
    }
  }

  /** kind: "speak" ducks other apps; "listen" asks them to pause while the microphone is open. */
  fun requestFocus(kind: String): Boolean {
    abandon()
    val current = ++generation
    val listen = kind == "listen"
    val attributes = AudioAttributes.Builder()
      .setUsage(AudioAttributes.USAGE_ASSISTANT)
      .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
      .build()
    val gain = if (listen) AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_EXCLUSIVE else AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK
    val built = AudioFocusRequest.Builder(gain)
      .setAudioAttributes(attributes)
      .setWillPauseWhenDucked(true)
      .setOnAudioFocusChangeListener({ change ->
        // Ignore callbacks for requests we already replaced or abandoned.
        if (current == generation) emit("onAudioFocusChange", mapOf("change" to focusName(change), "kind" to kind) + state())
      }, handler)
      .build()
    request = built
    return audio.requestAudioFocus(built) == AudioManager.AUDIOFOCUS_REQUEST_GRANTED
  }

  fun abandon() {
    request?.let { audio.abandonAudioFocusRequest(it) }
    request = null
    generation++
  }

  fun state(): Map<String, Any?> {
    val outputs = audio.getDevices(AudioManager.GET_DEVICES_OUTPUTS).mapNotNull { routeName(it.type) }.distinct()
    val preferred = listOf("bluetooth", "wired", "usb", "hdmi").firstOrNull { it in outputs } ?: "speaker"
    val mode = audio.mode
    return mapOf(
      "outputs" to outputs,
      "route" to preferred,
      "mode" to mode,
      "inCall" to (mode == AudioManager.MODE_IN_CALL || mode == AudioManager.MODE_IN_COMMUNICATION ||
        mode == AudioManager.MODE_RINGTONE),
      "volume" to audio.getStreamVolume(AudioManager.STREAM_MUSIC),
      "maxVolume" to audio.getStreamMaxVolume(AudioManager.STREAM_MUSIC)
    )
  }

  private fun focusName(change: Int): String = when (change) {
    AudioManager.AUDIOFOCUS_GAIN -> "gain"
    AudioManager.AUDIOFOCUS_LOSS -> "loss"
    AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> "loss_transient"
    AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK -> "duck"
    else -> "other"
  }

  private fun routeName(type: Int): String? = when (type) {
    AudioDeviceInfo.TYPE_BUILTIN_SPEAKER -> "speaker"
    AudioDeviceInfo.TYPE_BUILTIN_EARPIECE -> "earpiece"
    AudioDeviceInfo.TYPE_WIRED_HEADPHONES, AudioDeviceInfo.TYPE_WIRED_HEADSET -> "wired"
    AudioDeviceInfo.TYPE_BLUETOOTH_A2DP, AudioDeviceInfo.TYPE_BLUETOOTH_SCO -> "bluetooth"
    AudioDeviceInfo.TYPE_USB_HEADSET, AudioDeviceInfo.TYPE_USB_DEVICE -> "usb"
    AudioDeviceInfo.TYPE_HDMI -> "hdmi"
    else -> if (Build.VERSION.SDK_INT >= 31 && (type == AudioDeviceInfo.TYPE_BLE_HEADSET || type == AudioDeviceInfo.TYPE_BLE_SPEAKER)) "bluetooth" else null
  }
}
