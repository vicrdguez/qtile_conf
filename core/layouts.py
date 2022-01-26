from libqtile import layout
from libqtile.config import Match
from theme import colors
from libqtile.log_utils import logger

logger.warning("layouts")

layout_theme = {
       "border_width": 2,
       "margin": 10,
       "border_focus": colors['yellow'][0],
       }

layouts = [
    layout.MonadTall(**layout_theme),
    # layout.RatioTile(**layout_theme),
    layout.Matrix(**layout_theme),
    # layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Zoomy(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        ],
    border_focus=colors["altred"][0]
    )
