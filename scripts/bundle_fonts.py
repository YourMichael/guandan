"""把 Google 字体下载进 www/fonts，让 App 断网也能显示可爱字体。
任何一步失败都不改动 index.html（App 会改用联网字体或系统字体），构建照常进行。"""
import os, re, sys, urllib.request

HTML = "www/index.html"
OUT = "www/fonts"
UA = ("Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36")

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def main():
    html = open(HTML, encoding="utf-8").read()
    m = re.search(r'<link href="(https://fonts\.googleapis\.com/css2[^"]+)" rel="stylesheet">', html)
    if not m:
        print("未找到 Google 字体链接，跳过"); return
    css = get(m.group(1).replace("&amp;", "&")).decode("utf-8")
    os.makedirs(OUT, exist_ok=True)
    urls = sorted(set(re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", css)))
    print(f"下载 {len(urls)} 个字体文件…")
    for i, u in enumerate(urls):
        name = f"f{i}" + os.path.splitext(u.split("?")[0])[1]
        open(os.path.join(OUT, name), "wb").write(get(u))
        css = css.replace(u, name)
    open(os.path.join(OUT, "fonts.css"), "w", encoding="utf-8").write(css)
    html = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", html)
    html = html.replace(m.group(0), '<link href="fonts/fonts.css" rel="stylesheet">')
    open(HTML, "w", encoding="utf-8").write(html)
    print("字体已内置")

try:
    main()
except Exception as e:
    print("字体下载失败，改用联网字体：", e)
    sys.exit(0)
