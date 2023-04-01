from os import listdir
from os.path import isfile, join
import subprocess
from logger.logger import logger
import argparse
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    path = Path(args.path)
    # path = "scripts_dummy"
    scripts = [
        join(path, f)
        for f in listdir(path)
        if isfile(join(path, f)) and f.endswith(".sh")
    ]

    scripts.sort()
    n_scripts = len(scripts)
    logger.info(f"    Starting execute scripts in {path}")
    for i, s in enumerate(scripts):
        logger.debug(f"    {i + 1}/{n_scripts} - Starting to run script: {s}")

        a = subprocess.run(["sh", s], capture_output=True)

        if a.returncode == 0:
            logger.debug(
                f"Script {s} finished successfully!\n    The output was:\n    {a.stdout}"
            )
        else:
            logger.error(
                f"Script {s} failed!\n    The output was:\n    {a.stdout}\n    The error was:\n    {a.stderr}"
            )
    logger.info(f"    Finished execute scripts in {path}")
