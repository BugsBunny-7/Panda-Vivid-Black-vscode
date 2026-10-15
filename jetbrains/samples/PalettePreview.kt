// Types: blue · functions: purple · properties/argument labels: cyan
// Ordinary local variables and parameters: gray-white
class PalettePreview(val title: String, val enabled: Boolean) {
    fun render(context: String): String {
        val message = "$context: $title"
        return if (enabled) message else "Panda Modern Dark"
    }
}

fun preview(): String {
    val page = PalettePreview(title = "Panda", enabled = true)
    return page.render(context = "Preview")
}
