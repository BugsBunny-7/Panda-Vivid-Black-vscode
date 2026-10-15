// Class and return types stay blue; fields are cyan; methods are purple.
public class PalettePreview {
    private final String title = "Panda Modern Dark";

    public String render(String context) {
        final String message = context + ": " + title;
        return message;
    }

    @Override
    public String toString() {
        return render("Preview");
    }
}
