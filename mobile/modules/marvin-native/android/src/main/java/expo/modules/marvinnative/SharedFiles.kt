package expo.modules.marvinnative

import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.provider.OpenableColumns
import java.io.File
import java.util.UUID

/**
 * Copies files received from the Android share sheet into the app cache, so JS
 * works with plain file:// paths and the content:// grant can expire safely.
 */
object SharedFiles {
  private const val MAX_BYTES = 25L * 1024 * 1024

  fun fromIntent(context: Context, intent: Intent?): Map<String, Any?>? {
    if (intent == null) return null
    val action = intent.action
    if (action != Intent.ACTION_SEND && action != Intent.ACTION_SEND_MULTIPLE) return null
    val uris = mutableListOf<Uri>()
    if (action == Intent.ACTION_SEND) {
      stream(intent)?.let { uris.add(it) }
    } else {
      streams(intent)?.let { uris.addAll(it) }
    }
    val text = intent.getStringExtra(Intent.EXTRA_TEXT)
    // Consume the intent once: a configuration change must not re-deliver it.
    intent.action = null
    val files = uris.take(10).mapNotNull { copy(context, it) }
    if (files.isEmpty() && text.isNullOrBlank()) return null
    return mapOf("files" to files, "text" to text?.take(20000))
  }

  @Suppress("DEPRECATION")
  private fun stream(intent: Intent): Uri? =
    if (Build.VERSION.SDK_INT >= 33) intent.getParcelableExtra(Intent.EXTRA_STREAM, Uri::class.java)
    else intent.getParcelableExtra(Intent.EXTRA_STREAM)

  @Suppress("DEPRECATION")
  private fun streams(intent: Intent): List<Uri>? =
    if (Build.VERSION.SDK_INT >= 33) intent.getParcelableArrayListExtra(Intent.EXTRA_STREAM, Uri::class.java)
    else intent.getParcelableArrayListExtra(Intent.EXTRA_STREAM)

  private fun copy(context: Context, uri: Uri): Map<String, Any?>? {
    val resolver = context.contentResolver
    var name = "arquivo"
    var size = -1L
    resolver.query(uri, arrayOf(OpenableColumns.DISPLAY_NAME, OpenableColumns.SIZE), null, null, null)?.use { cursor ->
      if (cursor.moveToFirst()) {
        cursor.getString(0)?.let { name = it }
        if (!cursor.isNull(1)) size = cursor.getLong(1)
      }
    }
    val mime = resolver.getType(uri)
    val safeName = name.replace(Regex("[\\\\/:*?\"<>|\\x00-\\x1f]"), "_").take(180).ifBlank { "arquivo" }
    if (size > MAX_BYTES) {
      return mapOf("name" to safeName, "mimeType" to mime, "size" to size.toDouble(), "uri" to null,
        "error" to "Arquivo maior que 25 MB.")
    }
    val directory = File(context.cacheDir, "shared/" + UUID.randomUUID()).apply { mkdirs() }
    val target = File(directory, safeName)
    var copied = 0L
    try {
      resolver.openInputStream(uri)?.use { input ->
        target.outputStream().use { output ->
          val buffer = ByteArray(64 * 1024)
          while (true) {
            val read = input.read(buffer)
            if (read < 0) break
            copied += read
            if (copied > MAX_BYTES) throw IllegalStateException("too large")
            output.write(buffer, 0, read)
          }
        }
      } ?: return null
    } catch (_: Exception) {
      target.delete()
      return mapOf("name" to safeName, "mimeType" to mime, "size" to copied.toDouble(), "uri" to null,
        "error" to if (copied > MAX_BYTES) "Arquivo maior que 25 MB." else "Não foi possível ler o arquivo compartilhado.")
    }
    return mapOf("name" to safeName, "mimeType" to mime, "size" to copied.toDouble(), "uri" to Uri.fromFile(target).toString(),
      "error" to null)
  }
}
