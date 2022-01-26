from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from core.keybindings import mod, keys

from libqtile.log_utils import logger

logger.warning("grousp")


groups = [
            Group("1", label="  "),
            Group("1", label="  "),
            Group("2", matches=[Match(wm_class=["Firefox", "Brave-browser"])], label="  "),
            Group("3", label="  "),
            Group("4", matches=[Match(wm_class=["Alacritty"])], label="  "),
            Group("5", matches=[Match(wm_class=["zoom", "teams"])], label="  "),
            Group("6", matches=[Match(wm_class=["Slack"])], label="  "),
            Group("7", label="  "),
            Group("8", label="  "),
            Group("9", label="  "),
        ]

# groups = [
#             Group("1", label="dev"),
#             Group("2", label="www"),
#             Group("3", label="doc"),
#             Group("4", label="cli"),
#             Group("5", label="zoom"),
#             Group("6", label="chat"),
#             Group("7", label="mus"),
#             Group("8", label="vid"),
#             Group("9", label="misc"),
#         ]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
