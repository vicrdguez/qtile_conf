from libqtile.config import Drag, Click
from libqtile.command import lazy
from core.keybindings import mod
from libqtile.log_utils import logger

logger.warning("mouse")

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
        ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
        ),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
