import os
from pathlib import Path

LINE = "Optimizer"

assert 1 <= len(LINE) <= 24 and " " not in LINE, "exactly one word"

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
