#!/usr/bin/env python3
"""Validate local Cursor files and derive the install link. No network calls."""
import base64
import json
import re
from pathlib import Path
from urllib.parse import quote, urlparse
import xml.etree.ElementTree as ET

# Preserve the invoked path so a symlink in the shipped scripts path is visible.
ROOT = Path(__file__).absolute().parents[1]
DISTRIBUTABLE_FILES = (
    '.cursor-plugin/plugin.json', '.gitignore', 'ADD-TO-CURSOR.md',
    'LICENSE', 'README.md', 'assets/precision.svg', 'assets/precision-512.png',
    'assets/precision-ai-os-logo-512.png', 'mcp.json', 'scripts/prepare.py',
)


def regular_input(name):
    path = ROOT
    for part in Path(name).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('Symlink in distributable input: ' + name)
    if not path.is_file():
        raise ValueError('Missing distributable input: ' + name)
    return path


def asset_input(reference):
    if not isinstance(reference, str):
        raise ValueError('Expected a packaged asset path')
    path = Path(reference)
    if path.is_absolute() or '..' in path.parts or path.as_posix() not in DISTRIBUTABLE_FILES:
        raise ValueError('Manifest asset is not in public package allowlist: ' + reference)
    return regular_input(path.as_posix())


def check_local_references(value):
    if isinstance(value, dict):
        for item in value.values():
            check_local_references(item)
    elif isinstance(value, list):
        for item in value:
            check_local_references(item)
    elif isinstance(value, str) and value.startswith(('./', 'assets/')):
        asset_input(value)


def main():
    for name in DISTRIBUTABLE_FILES:
        regular_input(name)
    manifest = json.loads((ROOT / '.cursor-plugin/plugin.json').read_text())
    assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', manifest['name'])
    assert manifest['license'] == 'MIT'
    config = json.loads((ROOT / 'mcp.json').read_text())
    assert set(config) == {'mcpServers'}
    assert set(config['mcpServers']) == {'precision'}
    server = config['mcpServers']['precision']
    assert set(server) == {'url'}  # No headers, credentials or user variables.
    url = urlparse(server['url'])
    assert url.scheme == 'https' and url.netloc and not url.username
    assert not url.query and not url.fragment and '${' not in server['url']
    check_local_references(manifest)
    for field in ['logo', 'composerIcon', 'logoDark', 'composerIconDark']:
        if field in manifest:
            asset_input(manifest[field])
    for reference in manifest.get('screenshots', []):
        asset_input(reference)
    assert ET.parse(asset_input(manifest['logo'])).getroot().attrib['viewBox'] == '0 0 48 48'
    encoded = base64.b64encode(json.dumps(server, separators=(',', ':')).encode()).decode()
    link = ('cursor://anysphere.cursor-deeplink/mcp/install?name=precision&config='
            + quote(encoded, safe=''))
    text = ('# Add Precision AI OS to Cursor\n\n'
            'Generated from `mcp.json` by `python3 scripts/prepare.py`.\n\n'
            '[Add to Cursor](' + link + ')\n\n'
            'Cursor asks before installing. Sign in with your firm operator account.\n')
    (ROOT / 'ADD-TO-CURSOR.md').write_text(text)
    assert json.loads(base64.b64decode(encoded)) == server
    print('PASS: documented Cursor manifest/config constraints, local logo, no variables, deeplink round trip')
    print(link)


if __name__ == '__main__':
    main()
