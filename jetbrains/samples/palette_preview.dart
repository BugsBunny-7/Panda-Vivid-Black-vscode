// Dart fields/getters: cyan. Types/constructors: blue. Methods: purple.
// Named argument labels share the ordinary parameter-reference color
// in the JetBrains Dart plugin, so both remain gray-white here.
class PalettePreview {
  final String title;
  const PalettePreview({required this.title});

  String render(String context) {
    final message = '$context: $title';
    return message;
  }
}

void main() {
  final page = PalettePreview(title: 'Panda Modern Dark');
  print(page.render('Preview'));
}
