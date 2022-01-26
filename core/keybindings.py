from libqtile.config import Key
from libqtile.command import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger

logger.warning("keybindings")

mod = "mod4"
terminal = guess_terminal()


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<30} {}".format(mods, k.desc + "\n")

    return key_help


keys = [
    # Essentials
    Key([mod], "Return",
        lazy.spawn(".config/qtile/bin/qterm"),
        desc="Launch terminal"
        ),
    Key([mod], "BackSpace",
        lazy.window.kill(),
        desc="Kill focused window"
        ),
    Key([mod, "shift"], "Return",
        # lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
        lazy.spawn(".config/qtile/rofi/bin/launcher"),
        # lazy.spawn("rofi -show combi"),
        desc="Open rofi"
        ),
    Key([mod], "space",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"
        ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
        ),
    # LAUNCH
    Key([mod, "shift"], "n",
        lazy.spawn("nmd"),
        desc=""
        ),
    Key([mod], "Tab",
        lazy.spawn(".config/qtile/rofi/bin/windows"),
        desc="Shutdown Qtile"
        ),
    Key([mod, "shift"], "m",
        lazy.spawn(".config/qtile/rofi/bin/mpd"),
        desc="Shutdown Qtile"
        ),
    Key([mod, "shift"], "x",
        lazy.spawn(".config/qtile/rofi/bin/powermenu"),
        desc="Shutdown Qtile"
        ),
    Key([mod, "shift"], "r",
        lazy.spawn(".config/qtile/rofi/bin/asroot"),
        desc="Shutdown Qtile"
        ),
    Key([mod, "mod1"], "t",
        lazy.spawn(".config/qtile/rofi/bin/themes"),
        desc="Change Qtile themes"
        ),
    # Switch focus to specific monitor
    Key([mod], "e",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "w",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),
    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    # Window control
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus to left"
        ),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "h",
        lazy.layout.left(),
        desc='Move focus left'
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc='Move focus right'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move window up in the current stack"
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move window down in the current stack"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
        ),
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window up"
        ),
    Key([mod, "control"], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    # Stack controls
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    # Media controls
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Next song"
        ),
    Key([], "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Previous song"
        ),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="toggle play pause"
        ),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 10%+"),
        desc="Raise volume"
        ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 10%-"),
        desc="Lower volume"
        ),
    Key([], "XF86AudioMute",
        lazy.spawn("amixer set Master toggle"),
        desc="Lower volume"
        ),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("xbacklight +10")
        ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("xbacklight -10")
        ),
    # Key([mod], "p",
    #     lazy.spawn("bwmenu"), #Bitwarden with rofi
    #     desc="Bitwarden in rofi"
    #     ),
]

# keys.extend([
#     Key([mod], "F1",
#         lazy.spawn("sh -c 'echo \"" + show_keys() + "\" | rofi -dmenu -i -mesg \"Keyboard shortcuts\"'"),
#         desc="Print keyboard bindings"
#         ),
# ])
