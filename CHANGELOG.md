# Changelog

## 1.3.2 — 2026-11-24

- Add source-derived palette previews for all four themes across Dart/Flutter, Kotlin, Go, Rust and C++, refresh extension metadata, and document Flutter Dark activation and numeric color overrides. Syntax colors are unchanged from 1.3.1.

## 1.3.1 — 2026-11-20

- Change Panda Flutter Dark numeric literals from gray to `#AFCEA2`, matching Panda Modern Cyan. Includes integers, decimals, and hexadecimal literals; annotation colors are unchanged.

## 1.3.0 — 2026-11-19

- Add Panda Flutter Dark, a recreation of the official DartPad / Flutter dark syntax colors on the Modern Dark / Modern Cyan near-black interface (`#0C0C0C` background): green keywords (`#50E191`), orange types and literals (`#FF916E`), cyan identifiers, functions, properties, and named arguments (`#00D2FA`), pink strings (`#FA557D`), gray numbers and annotations (`#909090`), and blue-gray comments (`#909CC3`). Existing themes are unchanged.

## 1.2.1 — 2026-11-18

- Panda Modern Cyan: property access, fields, and getters use purple (`#B084FF`) in Dart, TypeScript, JavaScript, and Vue; member method calls such as `.map()` and `User.fromJson()` use blue (`#79B8FF`). Function and method declarations, plain function calls, named argument labels, and object keys keep their colors.

## 1.2.0 — 2026-11-18

- Add Panda Modern Cyan, a standalone variant of Panda Modern Dark.
- Use cyan (`#00C9B0`) for types and class names, and blue (`#79B8FF`) for properties and Dart named argument labels.
- Keep keywords, functions, strings, annotations, and the Modern Dark UI colors unchanged.


## 1.1.1 — 2026-10-10

- Use cyan (`#00D2F9`) for properties and Dart named argument labels in Panda Modern Dark.
- Preserve blue class and return type names, purple functions, and gray-white ordinary variables and parameters.

## 1.1.0 — 2026-10-07

- Add Panda Modern Dark alongside Panda Vivid Black, based on a complete VS Code 2026 Dark snapshot.
- Introduce near-black surfaces, orange keywords, blue types, purple functions, green strings, and gray-white properties and parameters in Panda Modern Dark.
- Align Dart syntax and common semantic token colors, with neutral brackets, readable CodeLens text, and consistent gold annotations.
- Bundle the frozen base theme, palette notes, and third-party license notices.
- Keep Panda Vivid Black's existing colors unchanged. Select either theme from Preferences: Color Theme.

## 1.0.0

- First Marketplace release of Panda Vivid Black.
- Near-black editor and terminal surfaces with vivid syntax and semantic token colors.
- Readable comments, completion selections, text selections, and Git diff backgrounds.
- Consistent dark status bars and blue active interface accents.
- New panda icon and English / Chinese documentation.
