"""Produce palette preview data from theme semantic colors; output JSON to stdout."""
import json
import re
import html
from pathlib import Path
root = Path(__file__).resolve().parent.parent
lines = [
 [('keyword','class '),('type','PreviewCard'),('text',' {')],
 [('annotation','  @override')],
 [('type','  Widget '),('function','build'),('text','('),('type','BuildContext '),('variable','context'),('text',') {')],
 [('keyword','    return '),('type','Container'),('text','(')],
 [('property','      width'),('text',': '),('number','100'),('text',',')],
 [('property','      height'),('text',': '),('number','100'),('text',',')],
 [('property','      color'),('text',': '),('keyword','const '),('type','Color'),('text','('),('number','0xFFD8D8D7'),('text','),')],
 [('property','      padding'),('text',': '),('type','EdgeInsets'),('text','.'),('function','all'),('text','('),('number','5.0'),('text','),')],
 [('property','      child'),('text',': '),('type','Text'),('text','('),('string',"'Panda Flutter'"),('text','),')],
 [('comment','      // Numbers: 100, 5.0, 0xFFD8D8D7')],
 [('text','    );')], [('text','  }')], [('text','}')]]
samples = {"dart": {"label": "Dart / Flutter", "lines": lines}}
for key, sample in json.loads((root/'tools/language-samples.json').read_text()).items():
    parsed = []
    for line in sample['code'].splitlines():
        segments, end = [], 0
        for match in re.finditer(r'\{([a-z]+)\|([^{}]*)\}', line):
            if match.start() > end:
                segments.append(('text', line[end:match.start()]))
            segments.append((match[1], html.unescape(match[2])))
            end = match.end()
        segments.append(('text', line[end:]))
        parsed.append(segments)
    samples[key] = {'label': sample['label'], 'lines': parsed}
previews=[]
for p in sorted((root/'themes').glob('*-color-theme.json')):
 d=json.loads(p.read_text());sem=d['semanticTokenColors'];colors=d['colors']
 palette={'text':colors['editor.foreground']}
 for role in ['keyword','type','function','variable','property','string','number','comment','annotation']:
  v=sem.get(role,sem.get({'number':'numberLiteral','annotation':'annotation:dart'}.get(role,''),'#E8E8E8'))
  palette[role]=v['foreground'] if isinstance(v,dict) else v
 slug=p.stem.replace('-color-theme','')
 for key, sample in samples.items():
  filename = slug if key == 'dart' else slug + '-' + key
  previews.append(dict(slug=filename,name=d.get('name',slug),language=sample['label'],background=colors['editor.background'],lines=[[dict(text=t,color=palette[r]) for r,t in line] for line in sample['lines']]))
print(json.dumps(previews))
