# Panda Vivid Black

A dark theme that fuses **Panda Syntax** token semantics with the **near-black Vivid Black** UI shell.

## Credits

- Token semantics & palette: [Panda Syntax](https://github.com/siamak/panda-syntax-vscode) by Siamak Mokhtari
- UI shell & vivid accents: Dracula Dark Vivid Black by BennyWu

## Recommended font

This theme is tuned for **Operator Mono** (italic-heavy token styling). Set in VS Code settings:

```json
{
  "editor.fontFamily": "'Operator Mono', Menlo, Monaco, monospace",
  "editor.fontLigatures": true
}
```

## Palette

| Token | Color |
| --- | --- |
| Keyword | `#FF6BA8` pink |
| String | `#19F9D8` teal |
| Function | `#4FB6FF` blue |
| Type / Class | `#19F9D8` teal (italic) |
| Constant / Storage | `#FFA647` orange |
| Number / Boolean | `#A970FF` purple |
| Parameter | `#FF8A3D` orange (italic) |
| Property | `#00CFFF` cyan |
| Tag | `#FF2D8D` magenta |
| Comment | `#6B6E80` gray (italic) |

## Highlighting during startup

Basic syntax highlighting and semantic highlighting share the same palette for recognized types, functions, keywords, and comments. Types are teal and italic before the language server is ready. Semantic highlighting remains enabled and can refine identifiers once project analysis completes.

The editor, editor gutter, minimap, panel, and terminal use `#0b0b0e` directly from the theme; no user color override is required.
