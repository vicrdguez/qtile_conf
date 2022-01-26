from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from widgets import primary_widgets, secondary_widgets
# import subprocess

logger.warning("screens")

def status_bar(widgets, size=24):
    return bar.Bar(widgets, size, opacity=1)


screens = [
        Screen(top=status_bar(primary_widgets, 34)),
        Screen(top=status_bar(secondary_widgets, 36)),
        ]
# screens = [
#     Screen(
#         top=bar.Bar(
#             primary_widgets,
#             34,
#         ),
#     ),
#     Screen(
#         top=bar.Bar(
#             primary_widgets,
#             24,
#         ),
#     ),
# ]
