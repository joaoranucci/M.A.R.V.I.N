package expo.modules.marvinnative

import android.app.Application
import android.content.Context
import expo.modules.core.interfaces.ApplicationLifecycleListener
import expo.modules.core.interfaces.Package

/** Runs in Application.onCreate, before React Native builds its OkHttp client. */
class MarvinNativePackage : Package {
  override fun createApplicationLifecycleListeners(context: Context?): List<ApplicationLifecycleListener> =
    listOf(object : ApplicationLifecycleListener {
      override fun onCreate(application: Application) {
        MarvinTls.load(application)
        MarvinTls.install()
      }
    })
}
