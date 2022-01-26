from libqtile import widget
from theme import colors
from libqtile.log_utils import logger

logger.warning("bar")


def base(fg='text', bg='dark'):
    return {
            'foreground': colors[fg],
            'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",   # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces():
    return [
        separator(),
        icon(text=""),  # arch Icon: nf-linux-archlinux
        widget.GroupBox(
            **base(fg='light'),
            font='Iosevka',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.TaskList(
            **base(fg='focus'),
            padding=5,
            highlight_method='block'),
        # widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
        *workspaces(),
        separator,
        powerline('color4', 'dark'),
        widget.Net(**base(bg='color3'), interface='wlp2s0'),
        powerline('color3', 'color4'),
        widget.Memory(
            foreground=colors[2],
            background=colors[5],
            format='{MemPercent}%',
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')
                },
            padding=5
            ),
        powerline('color4', 'color3')
        icon(bg="color1", fontsize=17, text=' '),  # Icon: nf-mdi-calendar_clock
        widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
        powerline('dark', 'color1'),
        widget.Systray(background=colors['dark'], padding=5),
        widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
]


widget_defaults = {
        'font': 'Iosevka',
        'fontsize': 15,
        'padding': 3,
}
extension_defaults = widget_defaults.copy()
