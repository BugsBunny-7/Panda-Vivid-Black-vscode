#!/usr/bin/env python3
"""Validate and archive the resource-only theme; no compiler or SDK download."""
import io
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parent
RESOURCES = ROOT / 'resources'


def archive(entries):
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as bundle:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 12, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data)
    return output.getvalue()


def main():
    plugin = ET.parse(RESOURCES / 'META-INF/plugin.xml').getroot()
    version = plugin.findtext('version')
    assert version and re.fullmatch(r'\d+\.\d+\.\d+', version)
    assert plugin.findtext('depends') == 'com.intellij.modules.platform'
    provider = plugin.find('extensions/themeProvider')
    theme = json.loads((RESOURCES / provider.attrib['path'].lstrip('/')).read_text())
    scheme_path = RESOURCES / theme['editorScheme'].lstrip('/')
    scheme = ET.parse(scheme_path).getroot()
    assert scheme.attrib['name'] == theme['name'] == 'Panda Modern Dark'
    assert scheme.attrib['parent_scheme'] == 'Darcula' and theme['dark'] is True
    for value in theme['colors'].values():
        assert re.fullmatch(r'#[0-9A-Fa-f]{6}', value)
    for key, value in theme['ui'].items():
        assert value in theme['colors'] or re.fullmatch(r'#[0-9A-Fa-f]{6}', value), key
    attributes = {}
    for option in scheme.findall('attributes/option'):
        name = option.attrib['name']
        assert name not in attributes, name
        attributes[name] = {item.attrib['name']: item.attrib['value'] for item in option.findall('value/option')}
    for option in scheme.findall('colors/option'):
        assert re.fullmatch(r'[0-9A-Fa-f]{6}', option.attrib['value'])
    for values in attributes.values():
        assert re.fullmatch(r'[0-9A-Fa-f]{6}', values['FOREGROUND'])
        assert values['FONT_TYPE'] == '0'
    # Protect the approved distinction between properties, types, and ordinary parameters.
    source = json.loads((ROOT.parent / 'themes/panda-modern-dark-color-theme.json').read_text())
    roles = source['semanticTokenColors']
    for name, role in {
        'CLASS_NAME_ATTRIBUTES': 'class', 'KOTLIN_CLASS': 'class', 'DART_CLASS': 'class',
        'DART_CONSTRUCTOR': 'class', 'KOTLIN_CONSTRUCTOR': 'class',
        'METHOD_DECLARATION_ATTRIBUTES': 'function', 'KOTLIN_FUNCTION_CALL': 'function',
        'DART_INSTANCE_METHOD_REFERENCE': 'function',
        'INSTANCE_FIELD_ATTRIBUTES': 'property', 'KOTLIN_NAMED_ARGUMENT': 'property',
        'KOTLIN_INSTANCE_PROPERTY': 'property', 'DART_INSTANCE_GETTER_REFERENCE': 'property',
        'DART_INSTANCE_FIELD_REFERENCE': 'property',
        'PARAMETER_ATTRIBUTES': 'parameter', 'KOTLIN_PARAMETER': 'parameter',
        'DART_PARAMETER_REFERENCE': 'parameter', 'DART_DYNAMIC_PARAMETER_REFERENCE': 'parameter',
        'DART_LOCAL_VARIABLE_REFERENCE': 'variable', 'DART_ANNOTATION': 'annotation:dart',
    }.items():
        assert attributes[name]['FOREGROUND'] == roles[role].lstrip('#'), name
    entries = {p.relative_to(RESOURCES).as_posix(): p.read_bytes() for p in RESOURCES.rglob('*') if p.is_file()}
    entries['META-INF/LICENSE'] = (ROOT.parent / 'LICENSE').read_bytes()
    jar = archive(entries)
    name = f'panda-modern-dark-{version}'
    distribution = archive({f'panda-modern-dark/lib/{name}.jar': jar})
    # Verify the exact bytes to be delivered, including all referenced resources.
    with zipfile.ZipFile(io.BytesIO(distribution)) as outer:
        assert outer.testzip() is None
        with zipfile.ZipFile(io.BytesIO(outer.read(outer.namelist()[0]))) as inner:
            assert inner.testzip() is None
            assert inner.read('Panda Modern Dark.xml') == scheme_path.read_bytes()
            assert inner.read('META-INF/plugin.xml') == entries['META-INF/plugin.xml']
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    (dist / f'{name}.zip').write_bytes(distribution)
    (dist / 'Panda Modern Dark.icls').write_bytes(scheme_path.read_bytes())
    print(f'Validated {len(attributes)} syntax roles. Created {dist / (name + ".zip")}')
    print(f'Editor-only alternative: {dist / "Panda Modern Dark.icls"}')


if __name__ == '__main__':
    main()
