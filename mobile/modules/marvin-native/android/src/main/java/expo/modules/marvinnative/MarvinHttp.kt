package expo.modules.marvinnative

import android.content.Context
import android.net.Uri
import android.util.Base64
import expo.modules.kotlin.Promise
import java.io.ByteArrayOutputStream
import java.io.File
import java.io.IOException
import java.util.concurrent.ConcurrentHashMap
import okhttp3.Call
import okhttp3.Callback
import okhttp3.HttpUrl.Companion.toHttpUrl
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.Request
import okhttp3.RequestBody
import okhttp3.RequestBody.Companion.asRequestBody
import okhttp3.RequestBody.Companion.toRequestBody
import okhttp3.Response

/** Explicit transport, independent of the fetch implementation installed by Expo. */
object MarvinHttp {
  private data class Pending(val call: Call, val pin: String)
  private val requests = ConcurrentHashMap<String, Pending>()
  private val cancelled = mutableSetOf<String>()
  private val lock = Any()
  private const val MAX_RESPONSE = 32 * 1024 * 1024

  fun cancel(id: String) {
    synchronized(lock) {
      requests[id]?.call?.cancel() ?: run {
        if (cancelled.size >= 1024) cancelled.clear()
        cancelled.add(id)
      }
    }
  }

  fun pinsChanged() {
    val pins = MarvinTls.getPins()
    requests.values.filter { it.pin !in pins }.forEach { it.call.cancel() }
  }

  fun close() {
    requests.values.forEach { it.call.cancel() }
    requests.clear()
    synchronized(lock) { cancelled.clear() }
  }

  fun request(context: Context, options: Map<String, Any?>, promise: Promise) {
    var registeredId: String? = null
    try {
      val id = options["id"] as? String ?: error("id")
      require(id.isNotEmpty() && id.length <= 100 && !requests.containsKey(id))
      val pin = options["pin"] as? String ?: error("pin")
      val url = (options["url"] as? String ?: error("url")).toHttpUrl()
      require(url.isHttps && url.username.isEmpty() && url.password.isEmpty() && url.fragment == null && url.encodedPath.startsWith("/v1/"))
      val method = options["method"] as? String ?: "GET"
      require(method in setOf("GET", "POST", "PUT", "DELETE"))
      val timeout = ((options["timeoutMs"] as? Number)?.toLong() ?: 15000L).coerceIn(1000L, 300000L)
      val headers = options["headers"] as? Map<*, *> ?: emptyMap<String, String>()
      require(headers.size <= 32)
      val builder = Request.Builder().url(url)
      for ((key, value) in headers) {
        require(key is String && value is String && Regex("^[A-Za-z0-9-]+$").matches(key))
        require(key.lowercase() !in setOf("host", "cookie", "connection", "content-length", "proxy-authorization"))
        require(value.length <= 8192 && value.none { it.code < 32 || it.code == 127 })
        builder.header(key, value)
      }
      val upload = options["upload"] as? Map<*, *>
      val text = options["body"] as? String
      var body: RequestBody? = null
      if (upload != null) {
        require(method == "POST" && text == null)
        body = multipart(context, upload)
      } else if (text != null) {
        require(method != "GET" && text.toByteArray(Charsets.UTF_8).size <= 256 * 1024)
        body = text.toRequestBody("application/json; charset=utf-8".toMediaType())
      } else if (method == "POST" || method == "PUT") {
        body = ByteArray(0).toRequestBody(null)
      }
      val client = MarvinTls.gatewayClient(pin, timeout)
      val call = client.newCall(builder.method(method, body).build())
      synchronized(lock) {
        if (cancelled.remove(id)) {
          promise.reject("E_ABORTED", "Requisição cancelada.", null)
          return
        }
        require(requests.putIfAbsent(id, Pending(call, pin)) == null)
      }
      registeredId = id
      val binary = options["binary"] as? Boolean ?: false
      call.enqueue(object : Callback {
        private fun cleanup() {
          requests.remove(id)
          client.connectionPool.evictAll()
          client.dispatcher.executorService.shutdown()
        }

        override fun onFailure(call: Call, error: IOException) {
          cleanup()
          promise.reject(if (call.isCanceled()) "E_ABORTED" else "E_SECURE_TRANSPORT",
            "Falha na conexão segura com o PC. Confira endereço, rede e certificado.", null)
        }

        override fun onResponse(call: Call, response: Response) {
          try {
            response.use {
              val stream = response.body?.byteStream()
              val output = ByteArrayOutputStream()
              stream?.use { input ->
                val buffer = ByteArray(65536)
                while (true) {
                  val count = input.read(buffer)
                  if (count < 0) break
                  require(output.size() <= MAX_RESPONSE - count)
                  output.write(buffer, 0, count)
                }
              }
              val bytes = output.toByteArray()
              val encoded = binary && response.isSuccessful
              promise.resolve(mapOf("status" to response.code,
                "body" to if (encoded) Base64.encodeToString(bytes, Base64.NO_WRAP) else bytes.toString(Charsets.UTF_8),
                "binary" to encoded))
            }
          } catch (_: Exception) {
            promise.reject("E_SECURE_TRANSPORT", "Resposta do PC interrompida ou acima do limite.", null)
          } finally { cleanup() }
        }
      })
    } catch (_: Exception) {
      registeredId?.let { requests.remove(it)?.call?.cancel() }
      promise.reject("E_SECURE_TRANSPORT", "Requisição segura inválida ou indisponível nesta build.", null)
    }
  }

  private fun multipart(context: Context, upload: Map<*, *>): RequestBody {
    val description = upload["file"] as? Map<*, *> ?: error("file")
    val uri = Uri.parse(description["uri"] as? String ?: error("uri"))
    require(uri.scheme == "file")
    val file = File(uri.path ?: error("path")).canonicalFile
    require(listOf(context.filesDir, context.cacheDir).any { file.path.startsWith(it.canonicalPath + File.separator) })
    require(file.isFile && file.length() in 1..(20L * 1024 * 1024))
    val fields = upload["fields"] as? Map<*, *> ?: error("fields")
    require(fields.keys == setOf("client_id", "category"))
    val builder = MultipartBody.Builder().setType(MultipartBody.FORM)
    for (key in listOf("client_id", "category")) {
      val value = fields[key] as? String ?: error("field")
      require(value.toByteArray(Charsets.UTF_8).size <= 1024)
      builder.addFormDataPart(key, value)
    }
    val name = (description["name"] as? String ?: "documento").take(160).replace(Regex("[\\r\\n\"/\\\\]"), "_")
    val mime = (description["mimeType"] as? String)?.toMediaTypeOrNull() ?: "application/octet-stream".toMediaType()
    return builder.addFormDataPart("file", name, file.asRequestBody(mime)).build()
  }
}
