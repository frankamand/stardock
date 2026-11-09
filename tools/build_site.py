"""Build the GitHub Pages version of Star Dock from the Claude artifact source (stardock-artifact.html).
Usage: python3 tools/build_site.py path/to/stardock-artifact.html
Differences from the artifact: fonts load from ./fonts (works offline), app manifest + icons, offline service worker."""
import re, sys
src = open(sys.argv[1]).read()
fonts = """<style>
@font-face{font-family:'Orbitron';font-weight:700;font-display:swap;src:url(fonts/orbitron-latin-700-normal.woff2) format('woff2')}
@font-face{font-family:'Orbitron';font-weight:900;font-display:swap;src:url(fonts/orbitron-latin-900-normal.woff2) format('woff2')}
@font-face{font-family:'Share Tech Mono';font-weight:400;font-display:swap;src:url(fonts/share-tech-mono-latin-400-normal.woff2) format('woff2')}
</style>
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#0b0322">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="icon" type="image/png" href="icons/favicon-64.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">"""
src, n = re.subn(r'<link rel="preconnect" href="https://fonts.googleapis.com">\s*<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\s*<link href="https://fonts.googleapis.com/css2[^"]*" rel="stylesheet">', fonts, src)
assert n == 1, 'font block not found'
sw = """<script>
if ('serviceWorker' in navigator && location.protocol === 'https:') navigator.serviceWorker.register('sw.js').catch(() => {});
</script>
</body>"""
assert src.count('</body>') == 1
src = src.replace('</body>', sw)
open('index.html', 'w').write(src)
print('index.html built,', len(src), 'bytes')
