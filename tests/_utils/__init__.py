import sys
import subprocess
from os import PathLike
from typing import Union


def run_hatch_build(cwd: Union[str, PathLike[str]]):
    process = subprocess.run([sys.executable, "-m", "hatch", "build"], cwd=cwd)
    process.check_returncode()