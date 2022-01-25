#!/usr/bin/env bash

export PATH="${PATH}:$HOME/.config/qtile/bin"
## Get colors from .Xresources -------------------------------#
xrdb ~/.Xresources
getcolors () {
    FOREGROUND=$(xrdb -query | grep 'foreground:'| awk '{print $NF}')
    BACKGROUND=$(xrdb -query | grep 'background:'| awk '{print $NF}')
    BLACK=$(xrdb -query | grep 'color0:'| awk '{print $NF}')
    RED=$(xrdb -query | grep 'color1:'| awk '{print $NF}')
    GREEN=$(xrdb -query | grep 'color2:'| awk '{print $NF}')
    YELLOW=$(xrdb -query | grep 'color3:'| awk '{print $NF}')
    BLUE=$(xrdb -query | grep 'color4:'| awk '{print $NF}')
    MAGENTA=$(xrdb -query | grep 'color5:'| awk '{print $NF}')
    CYAN=$(xrdb -query | grep 'color6:'| awk '{print $NF}')
    WHITE=$(xrdb -query | grep 'color7:'| awk '{print $NF}')
}
getcolors

# Kill if already running
killall -9 xsettingsd dunst xfce4-power-manager picom

picom --experimental-backends --config ~/.config/qtile/picom.conf &

dunst \
-geom "280x50-10+42" -frame_width "1" -font "Iosevka Custom 9" \
-lb "$BACKGROUND" -lf "$FOREGROUND" -lfr "$BLUE" \
-nb "$BACKGROUND" -nf "$FOREGROUND" -nfr "$BLUE" \
-cb "$BACKGROUND" -cf "$RED" -cfr "$RED" &

xsettingsd &

# polkit agent
if [[ ! `pidof xfce-polkit` ]]; then
	/usr/lib/xfce-polkit/xfce-polkit &
fi

# Enable power management
xfce4-power-manager &

flameshot &
#nitrogen --restore &
~/.fehbg
blueman-applet &
nm-applet &
# scripts
# qtilecolors

