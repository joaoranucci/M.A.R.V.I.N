package expo.modules.marvinnative

import android.content.Context
import android.util.Base64
import com.facebook.react.modules.network.OkHttpClientFactory
import com.facebook.react.modules.network.OkHttpClientProvider
import java.io.IOException
import java.net.InetSocketAddress
import java.util.concurrent.TimeUnit
import okhttp3.OkHttpClient
import java.security.KeyStore
import java.security.MessageDigest
import java.security.cert.CertificateException
import java.security.cert.X509Certificate
import javax.net.ssl.HostnameVerifier
import javax.net.ssl.HttpsURLConnection
import javax.net.ssl.SSLContext
import javax.net.ssl.SSLSocket
import javax.net.ssl.TrustManagerFactory
import javax.net.ssl.X509TrustManager

/**
 * Trust for the MARVIN gateway's self-signed certificate.
 *
 * A certificate is accepted only when the SHA-256 of its public key (SPKI) equals a pin
 * received out-of-band (QR code or compared fingerprint). Every other host keeps the
 * normal Android validation, so public HTTPS is unaffected.
 */
object MarvinTls {
  private const val PREFS = "marvin_tls"
  private const val KEY = "pins"

  @Volatile
  private var pins: Set<String> = emptySet()

  fun load(context: Context) {
    pins = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getStringSet(KEY, emptySet())?.toSet() ?: emptySet()
  }

  fun setPins(context: Context, values: List<String>) {
    val clean = values.filter { Regex("^[A-Za-z0-9+/]{43}=$").matches(it) }.toSet()
    pins = clean
    context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putStringSet(KEY, clean).apply()
  }

  fun getPins(): List<String> = pins.toList()

  fun pinOf(cert: X509Certificate): String =
    Base64.encodeToString(MessageDigest.getInstance("SHA-256").digest(cert.publicKey.encoded), Base64.NO_WRAP)

  private fun isPinned(cert: X509Certificate?): Boolean {
    val current = pins
    return cert != null && current.isNotEmpty() && pinOf(cert) in current
  }

  private fun systemTrustManager(): X509TrustManager {
    val factory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm())
    factory.init(null as KeyStore?)
    return factory.trustManagers.filterIsInstance<X509TrustManager>().first()
  }

  private class PinningTrustManager(private val system: X509TrustManager) : X509TrustManager {
    override fun checkClientTrusted(chain: Array<out X509Certificate>, authType: String) =
      system.checkClientTrusted(chain, authType)

    override fun checkServerTrusted(chain: Array<out X509Certificate>, authType: String) {
      val leaf = chain.firstOrNull()
      if (leaf != null && isPinned(leaf)) {
        leaf.checkValidity()
        return
      }
      system.checkServerTrusted(chain, authType)
    }

    override fun getAcceptedIssuers(): Array<X509Certificate> = system.acceptedIssuers
  }

  /** Installed before React Native creates its networking client (fetch / XHR). */
  fun install() {
    val trustManager = PinningTrustManager(systemTrustManager())
    val sslContext = SSLContext.getInstance("TLS").apply { init(null, arrayOf(trustManager), null) }
    val defaultVerifier = HttpsURLConnection.getDefaultHostnameVerifier()
    val verifier = HostnameVerifier { host, session ->
      val leaf = try {
        session.peerCertificates.firstOrNull() as? X509Certificate
      } catch (_: Exception) {
        null
      }
      // The gateway's address may change (DHCP/VPN); its pinned key does not.
      isPinned(leaf) || defaultVerifier.verify(host, session)
    }
    OkHttpClientProvider.setOkHttpClientFactory(OkHttpClientFactory {
      // No HTTP cache: responses carry private data and the gateway sends no-store anyway.
      OkHttpClientProvider.createClientBuilder()
        .sslSocketFactory(sslContext.socketFactory, trustManager)
        .hostnameVerifier(verifier)
        .build()
    })
  }

  /** Dedicated gateway client: a system-trusted but unpinned certificate is still rejected before HTTP. */
  fun gatewayClient(expectedPin: String, timeoutMs: Long): OkHttpClient {
    require(expectedPin in pins) { "Gateway sem pin aceito" }
    val trustManager = PinningTrustManager(systemTrustManager())
    val context = SSLContext.getInstance("TLS").apply { init(null, arrayOf(trustManager), null) }
    val defaultVerifier = HttpsURLConnection.getDefaultHostnameVerifier()
    return OkHttpClientProvider.createClientBuilder()
      .sslSocketFactory(context.socketFactory, trustManager)
      .hostnameVerifier { host, session ->
        val leaf = session.peerCertificates.firstOrNull() as? X509Certificate
        isPinned(leaf) || defaultVerifier.verify(host, session)
      }
      .followRedirects(false)
      .followSslRedirects(false)
      .callTimeout(timeoutMs, TimeUnit.MILLISECONDS)
      .connectTimeout(minOf(timeoutMs, 10000L), TimeUnit.MILLISECONDS)
      .readTimeout(timeoutMs, TimeUnit.MILLISECONDS)
      .writeTimeout(timeoutMs, TimeUnit.MILLISECONDS)
      .addNetworkInterceptor { chain ->
        val leaf = chain.connection()?.handshake()?.peerCertificates?.firstOrNull() as? X509Certificate
        if (leaf == null || expectedPin !in pins ||
          !MessageDigest.isEqual(expectedPin.toByteArray(Charsets.US_ASCII), pinOf(leaf).toByteArray(Charsets.US_ASCII))) {
          throw IOException("Impressão digital do gateway não confere")
        }
        leaf.checkValidity()
        chain.proceed(chain.request())
      }
      .build()
  }

  /**
   * Reads the certificate presented at host:port without sending any request,
   * so the user can compare its fingerprint with the one shown on the PC.
   */
  fun probe(host: String, port: Int): Map<String, Any?> {
    var captured: X509Certificate? = null
    val capture = object : X509TrustManager {
      override fun checkClientTrusted(chain: Array<out X509Certificate>, authType: String) =
        throw CertificateException("client")

      override fun checkServerTrusted(chain: Array<out X509Certificate>, authType: String) {
        captured = chain.firstOrNull()
      }

      override fun getAcceptedIssuers(): Array<X509Certificate> = emptyArray()
    }
    val context = SSLContext.getInstance("TLS").apply { init(null, arrayOf(capture), null) }
    (context.socketFactory.createSocket() as SSLSocket).use { socket ->
      socket.soTimeout = 6000
      socket.connect(InetSocketAddress(host, port), 6000)
      socket.startHandshake()
    }
    val cert = captured ?: throw CertificateException("Nenhum certificado recebido")
    cert.checkValidity()
    return mapOf(
      "pin" to pinOf(cert),
      "subject" to cert.subjectX500Principal.name,
      "notAfter" to cert.notAfter.time.toDouble()
    )
  }
}
