import sys
from pathlib import Path
module_path = str(Path.cwd().parents[0] / "agripy")
sys.path.insert(0, module_path)


def till():
    from test import pr
    return pr('test')


print(till())
