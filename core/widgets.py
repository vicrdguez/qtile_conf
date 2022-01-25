from libqtile import widget
from theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


def base(fg='foreground', bg='background'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=10)


def icon(fg='foreground', bg='background', fontsize=17, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="foreground", bg="background"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=70,
        padding=-5
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(),
            font='Iosevka',
            fontsize=27,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            # Groups with windows that are not focused
            active=colors['green'],
            # Groups without windows
            inactive=colors['foreground'],
            # asdasd
            highlight_colors=colors['magenta'],
            # selected group color in any screen
            block_highlight_text_color=colors['blue'],
            urgent_border=colors['red'],
            urgent_text=colors['red'],
            this_current_screen_border=colors['blue'],
            this_screen_border=colors['green'],
            other_current_screen_border=colors['blue'],
            other_screen_border=colors['green'],
            highlight_method='line',
            # urgent_alert_method='line',
            disable_drag=True,
            rounded=False,
        ),
        separator(),
        widget.WindowName(**base(fg='yellow')),
        # widget.TaskList(
        #     **base(),
        #     padding=0,
        #     highlight_method='line',
        #     border=colors['yellow']
        #     ),
        # separator(),
    ]


def init_widgets():
    """Generate a copy of the configured widgets for multiple screens."""
    widgets = [
        icon(fg='yellow', text='  ', fontsize=30),  # Icon nf-linux-archlinux
        *workspaces(),
        separator(),
        # powerline('blue', 'background'),
        icon(fg='blue', text="", fontsize=26),
        widget.ThermalSensor(
            **base(),
            threshold=90,
            padding=5
            ),
        separator(),
        # powerline('magenta', 'blue'),
        icon(fg='magenta', text="🖬"),
        widget.Memory(**base(), format='{MemPercent}%'),
        # powerline('green', 'magenta'),
        separator(),
        icon(fg='green', text='', fontsize=25),
        widget.PulseVolume(**base(), volume_app='pavucontrol'),
        separator(),
        # powerline("yellow", "green"),
        icon(fg="red", fontsize=25, text=''),  # Icon: nf-mdi-calendar_clock
        widget.Clock(**base(), format='%b %d - %H:%M '),
        separator(),
        # powerline('background', 'yellow'),
        widget.Systray(background=colors['background'], padding=0),
        separator(),
        widget.CurrentLayoutIcon(**base(fg='red'), scale=0.65),
    ]
    return widgets


primary_widgets = init_widgets()
secondary_widgets = init_widgets()

widget_defaults = {
    'font': 'Iosevka',
    'fontsize': 15,
    'padding': 3,
}
extension_defaults = widget_defaults.copy()
