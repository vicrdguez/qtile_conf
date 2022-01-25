import subprocess
from typing import List  # noqa: F401
from os import path
from libqtile import hook

from core.groups import groups
from core.keybindings import mod, keys
from core.layouts import layouts, floating_layout
from core.widgets import widget_defaults, extension_defaults
from core.screens import screens
from core.mouse import mouse
from core.path import qtile_path

# @hook.subscribe.startup
# def start():
#     subprocess.call(path.join(qtile_path, 'bin/qtilecolors'))
# 

@hook.subscribe.startup
def start_once():
    subprocess.call(path.join(qtile_path, 'autostart.sh'))


@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
