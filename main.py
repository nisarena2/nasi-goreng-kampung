import os
import shutil
from pathlib import Path

here = Path(__file__).resolve().parent
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
shutil.copyfile(here / "entry.png", out / "entry.png")
