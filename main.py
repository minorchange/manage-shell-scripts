from os import listdir
from os.path import isfile, join
import subprocess
from logger.logger import logger
import argparse
from pathlib import Path


def folderpath_from_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    return Path(args.path)


def scripfilepaths_from_folder(path):
    scripts = [
        join(path, f)
        for f in listdir(path)
        if isfile(join(path, f)) and f.endswith(".sh")
    ]
    scripts.sort()
    return scripts


if __name__ == "__main__":
    folder_path = folderpath_from_arg()
    scripts = scripfilepaths_from_folder(folder_path)

    logger.info(f"Starting execute scripts in {folder_path}")
    for i, s in enumerate(scripts):
        logger.debug(f"    {i + 1}/{len(scripts)} - Starting to run script: {s}")

        a = subprocess.run(["sh", s], capture_output=True)

        if a.returncode == 0:
            logger.debug(
                f"Script {s} finished successfully!\n    The output was:\n    {a.stdout}"
            )
        else:
            logger.error(
                f"Script {s} failed!\n    The output was:\n    {a.stdout}\n    The error was:\n    {a.stderr}"
            )
    logger.info(f"Finished execute scripts in {folder_path}")
