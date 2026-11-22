# -*- coding: utf-8 -*-
"""把 src/three-0.158.0.min.js 内联进 src/模拟农耕-模板.html，生成 index.html"""
from pathlib import Path

root = Path(__file__).resolve().parent
tpl = (root / "src" / "模拟农耕-模板.html").read_text(encoding="utf-8")
lib = (root / "src" / "three-0.158.0.min.js").read_text(encoding="utf-8")
needle = '<script src="three-0.158.0.min.js"></script>'

if needle not in tpl:
    raise SystemExit("模板里找不到 three.js 引用行")
if "</script" in lib:
    raise SystemExit("库文件里含 </script 字符串，需要转义处理")

out = tpl.replace(needle, "<script>\n" + lib + "\n</script>")
(root / "index.html").write_text(out, encoding="utf-8")
print("built:", root / "index.html", len(out.encode("utf-8")), "bytes")
