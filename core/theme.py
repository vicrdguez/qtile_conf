from os import path
import json
from libqtile.log_utils import logger

from path import qtile_path


def load():
    theme = path.join(qtile_path, "colors.json")
    logger.warning("THEME PATH: "+theme)
    if path.isfile(theme):
        with open(theme) as f:
            # logger.warning(f.read())
            return json.load(f)


if __name__ == "core.theme":
    colors = load()
