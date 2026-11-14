import os,shutil
from pathlib import Path
s=Path(__file__).parent/'entry.png'
d=Path(os.environ.get('MAKEFUN_OUTPUT_DIR','/output'))
d.mkdir(parents=True,exist_ok=True)
shutil.copyfile(s,d/'entry.png')
