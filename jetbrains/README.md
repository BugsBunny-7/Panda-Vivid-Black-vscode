# Panda Modern Dark — IntelliJ IDEA / Android Studio

根据已确认的 VS Code Panda Modern Dark **1.1.1** 配色移植。JetBrains 插件独立从 **1.0.0** 开始编号，同一个安装包用于 IntelliJ IDEA 和 Android Studio。

## 安装

1. 打开 IDE 的 **Settings → Plugins**。
2. 点击齿轮，选择 **Install Plugin from Disk…**，选择 `dist/panda-modern-dark-1.0.0.zip`。不要解压。
3. 如 IDE 提示重启，按提示操作。
4. 在 **Settings → Appearance & Behavior → Appearance → Theme** 中选择 **Panda Modern Dark**。
5. 如果编辑器仍是原配色，在 **Settings → Editor → Color Scheme** 中也选择 **Panda Modern Dark**。

只想修改编辑器颜色：在 **Editor → Color Scheme** 的菜单中选择 **Import Scheme…**，导入 `dist/Panda Modern Dark.icls`。这个文件不修改侧栏、菜单等 IDE 界面。

恢复原主题：在 Appearance 和 Color Scheme 中选回原来的主题与配色方案即可。

## 配色

| 用途 | 颜色 |
| --- | --- |
| 编辑器背景 | `#0C0C0C` |
| 标题、标签栏 | `#0F0F0F` |
| 类名、类型名、构造函数、返回类型 | `#79B8FF` |
| 属性、字段、Kotlin 命名参数标签 | `#00D2F9` |
| 函数和方法 | `#B084FF` |
| 普通变量和参数 | `#E8E8E8` |
| 关键字和运算符 | `#FF804F` |
| 字符串 | `#7EE787` |
| 注解 | `#FFA618` |
| 注释 | `#888888` |

包含 Java、Kotlin、Dart 以及 Android XML 布局的明确配色，其他语言使用通用语法角色或 Darcula 回退。保留 IDE 的错误、警告提示。主题不设置字体族、字号或行高，不包含可执行代码、语言服务或联网功能。

### Dart 与 VS Code 的差异

JetBrains Dart 插件使用分析服务器的旧式 `HighlightRegion` 分类；命名参数标签和普通参数引用共用 `DART_PARAMETER_REFERENCE` / `DART_DYNAMIC_PARAMETER_REFERENCE`。VS Code 的 `parameter.label:dart` 修饰符不能直接搬过来。

因此本版本中 Dart 的 `title:`、`body:` 等命名参数标签保持灰白，避免将 `context` 等普通参数也改成青蓝。Dart 字段、属性、getter/setter 采用青蓝；Kotlin 的命名参数标签有独立的 `KOTLIN_NAMED_ARGUMENT`，可以直接采用青蓝。主题不会通过额外分析插件改变语言行为。

Dart 的语义颜色需要安装并启用 Dart 插件；Flutter 项目使用 Flutter/Dart 插件。如果另行启用了语义彩虹色或第三方颜色覆盖，请在对应设置中关闭覆盖后比较。语义分析完成前的基础高亮可能与完成后不同。

## 本地打包

在仓库根目录运行：

```sh
python3 jetbrains/package.py
```

仅使用 Python 标准库，校验资源后封装 JAR/ZIP；无需 Gradle、JDK 编译或网络下载。输出安装 ZIP 和独立 `.icls`，位于 `jetbrains/dist/`。打包同时核对 VS Code 源主题中的关键语义配色，避免类名、普通参数等角色被误改。

## 验证记录与兼容范围

- 插件声明 IntelliJ Platform **243+（2024.3+）**，仅依赖平台模块，不强制依赖 Java、Kotlin 或 Dart 插件。
- 已通过 JSON/XML 解析、资源引用、安装包结构、ZIP 完整性和关键配色映射检查。
- 全部 71 个 UI 键与 223 个语法键已在本机 Android Studio **262.9437.185.2621.16467767** 的平台及 Java/Kotlin/Dart 插件定义中核对；Dart 插件版本为 **510.0.0**。
- 全部 UI 键和非 Dart 语法键也已在本机 IntelliJ IDEA **2026.2.3 / 262.10968.63** 的平台及语言插件定义中核对。
- 尚未在 IDEA 或 Android Studio 内安装并目视验收；243+ 是声明范围，不代表已逐版本测试。
- `samples/` 提供 Java、Kotlin、Dart 代码，可在已有项目中打开对照。优先检查：返回类型保持蓝色、字段为青蓝、普通参数保持灰白。
- 未发布到 JetBrains Marketplace，也未修改本机 IDE 的主题设置。

## 格式与映射依据

- [JetBrains 主题结构](https://plugins.jetbrains.com/docs/intellij/theme-structure.html)
- [JetBrains 编辑器配色格式](https://plugins.jetbrains.com/docs/intellij/themes-extras.html)
- [从磁盘安装插件](https://www.jetbrains.com/help/idea/managing-plugins.html)
- [Dart 分析服务器高亮分类](https://github.com/dart-lang/sdk/blob/main/pkg/analysis_server/lib/src/computer/computer_highlights.dart)

本主题为独立编写的 JetBrains 资源，使用仓库的 MIT 许可。通过 IDE 内置 Darcula 继承未覆盖项，不打包复制 JetBrains 的基础主题资源。
