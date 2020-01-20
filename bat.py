from math import floor

from util import poll, readline
import fmt
import icons

bat0 = "/sys/class/power_supply/BAT0/"
bat1 = "/sys/class/power_supply/BAT1/"
ac = "/sys/class/power_supply/AC/online"

b0_max = int(readline(bat0 + "energy_full", '0'))
b1_max = int(readline(bat1 + "energy_full", '0'))

warning_colors = [1, 9, 3, 11]

def get_bat():
    b0_val = int(readline(bat0 + "energy_now", '0'))
    b1_val = int(readline(bat1 + "energy_now", '0'))
    charging = int(readline(ac))

    percent = round((b0_val+b1_val) * 100 / (b0_max+b1_max))
    idx = floor(percent / 100 * 11)
    icon = icons.batc[idx] if charging else icons.bat[idx]
    if idx < len(warning_colors):
        icon = fmt.clr(icon, warning_colors[idx])

    return "{} {}%".format(icon, percent)

def bat():
    return poll(get_bat, 5)
