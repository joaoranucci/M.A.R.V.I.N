package expo.modules.marvinnative

import android.content.Context
import expo.modules.kotlin.exception.Exceptions
import expo.modules.kotlin.modules.Module
import expo.modules.kotlin.modules.ModuleDefinition

class MarvinNativeModule : Module() {
  private val context: Context
    get() = appContext.reactContext ?: throw Exceptions.ReactContextLost()

  private var monitor: AudioSessionMonitor? = null
  private var pendingShare: Map<String, Any?>? = null

  private fun audio(): AudioSessionMonitor =
    monitor ?: AudioSessionMonitor(context.applicationContext) { name, body -> sendEvent(name, body) }
      .also { monitor = it; it.start() }

  override fun definition() = ModuleDefinition {
    Name("MarvinNative")

    Events("onAudioFocusChange", "onAudioRouteChange", "onBecomingNoisy", "onCallStateChange", "onSharedFiles")

    OnCreate {
      audio()
    }

    OnDestroy {
      monitor?.stop()
      monitor = null
    }

    OnNewIntent { intent ->
      val shared = SharedFiles.fromIntent(context, intent) ?: return@OnNewIntent
      pendingShare = shared
      sendEvent("onSharedFiles", shared)
    }

    // ---- TLS pinning ----------------------------------------------------------------
    Function("setPinnedKeys") { pins: List<String> ->
      MarvinTls.setPins(context, pins)
    }

    Function("getPinnedKeys") {
      MarvinTls.getPins()
    }

    AsyncFunction("probeCertificate") { host: String, port: Int ->
      MarvinTls.probe(host, port)
    }

    // ---- audio session ----------------------------------------------------------------
    Function("requestAudioFocus") { kind: String ->
      audio().requestFocus(kind)
    }

    Function("abandonAudioFocus") {
      audio().abandon()
    }

    Function("getAudioState") {
      audio().state()
    }

    // ---- share sheet ------------------------------------------------------------------
    Function("consumeSharedFiles") {
      val launch = appContext.currentActivity?.intent
      val shared = pendingShare ?: SharedFiles.fromIntent(context, launch)
      pendingShare = null
      shared
    }
  }
}
