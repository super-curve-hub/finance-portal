import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
objects = []
for folder in ['concepts','dashboards','charts']:
    for p in (root/'data'/folder).glob('*.json'):
        d = json.loads(p.read_text(encoding='utf-8'))
        objects.append({
            'id': d.get('id'),
            'type': d.get('type'),
            'title': d.get('title'),
            'summary': d.get('summary'),
            'tags': d.get('tags', []),
            'related': d.get('related', [])
        })
(root/'api'/'search.json').write_text(json.dumps({'objects': objects}, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Built {len(objects)} objects')
