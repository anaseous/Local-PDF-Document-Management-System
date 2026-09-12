from pathlib import Path
import json, re
root=Path(__file__).resolve().parents[1]
required=['index.html','single-page/index.html','pwa/index.html','pwa/manifest.webmanifest','pwa/service-worker.js','pwa/icons/icon-192.png','pwa/icons/icon-512.png','pwa/icons/icon-maskable-512.png']
missing=[p for p in required if not (root/p).is_file()]
assert not missing, f"Missing files: {missing}"
m=json.loads((root/'pwa/manifest.webmanifest').read_text())
assert m['display']=='standalone'
assert {i['sizes'] for i in m['icons']} >= {'192x192','512x512'}
pwa=(root/'pwa/index.html').read_text(errors='ignore')
spa=(root/'single-page/index.html').read_text(errors='ignore')
assert 'rel="manifest"' in pwa and 'serviceWorker.register' in pwa
assert 'rel="manifest"' not in spa and 'serviceWorker.register' not in spa and 'id="pwaInstall"' not in spa
assert '<meta name="description"' in pwa and '<meta name="keywords"' in pwa
print('Validation passed')
