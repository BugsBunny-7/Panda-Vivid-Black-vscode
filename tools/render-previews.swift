// Run: swift tools/render-previews.swift <palette-data.json> <output-directory>
import AppKit
import Foundation
struct Segment: Decodable { let text: String; let color: String }
struct Preview: Decodable { let slug: String; let name: String; let language: String; let background: String; let lines: [[Segment]] }
func color(_ hex: String) -> NSColor {
    let rgb = UInt32(hex.dropFirst().prefix(6), radix: 16)!
    return NSColor(srgbRed: CGFloat((rgb >> 16) & 255)/255, green: CGFloat((rgb >> 8) & 255)/255, blue: CGFloat(rgb & 255)/255, alpha: 1)
}
let previews = try JSONDecoder().decode([Preview].self, from: Data(contentsOf: URL(fileURLWithPath: CommandLine.arguments[1])))
for preview in previews {
    let width = 1280, height = 780
    let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    let context = NSGraphicsContext(bitmapImageRep: rep)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = context
    color(preview.background).setFill()
    NSRect(x: 0, y: 0, width: width, height: height).fill()
    let font = NSFont(name: "OperatorMonoLocal-Book", size: 26) ?? NSFont.monospacedSystemFont(ofSize: 26, weight: .regular)
    func draw(_ text: String, _ x: CGFloat, _ y: CGFloat, _ c: String, _ f: NSFont) -> CGFloat {
        let attrs: [NSAttributedString.Key: Any] = [.font: f, .foregroundColor: color(c)]
        (text as NSString).draw(at: NSPoint(x: x, y: y), withAttributes: attrs)
        return (text as NSString).size(withAttributes: attrs).width
    }
    _ = draw(preview.name, 44, 710, "#ECE9E8", NSFont.systemFont(ofSize: 30, weight: .medium))
    _ = draw(preview.language + " · Palette preview", 44, 669, "#B8B8B8", NSFont.systemFont(ofSize: 18))
    for (index, line) in preview.lines.enumerated() {
        let y = CGFloat(606 - index * 36)
        _ = draw(String(format: "%2d", index+1), 40, y, "#777777", font)
        var x: CGFloat = 100
        for segment in line { x += draw(segment.text, x, y, segment.color, font) }
    }
    _ = draw("Illustrative token mapping · Not an editor screenshot", 44, 25, "#B8B8B8", NSFont.systemFont(ofSize: 17))
    NSGraphicsContext.restoreGraphicsState()
    let target = URL(fileURLWithPath: CommandLine.arguments[2]).appendingPathComponent(preview.slug + "-preview.png")
    try rep.representation(using: .png, properties: [:])!.write(to: target)
    print(target.path)
}
