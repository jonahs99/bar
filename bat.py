from math import floor

from util import poll, readline
import icons

bat0 = "/sys/class/power_supply/BAT0/"
bat1 = "/sys/class/power_supply/BAT1/"
ac = "/sys/class/power_supply/AC/online"

b0_max = int(readline(bat0 + "energy_full"))
b1_max = int(readline(bat1 + "energy_full"))

def get_bat():
    b0_val = int(readline(bat0 + "energy_now"))
    b1_val = int(readline(bat1 + "energy_now"))
    charging = int(readline(ac))

    percent = round((b0_val+b1_val) * 100 / (b0_max+b1_max))
    step = floor(percent / 100 * 11)
    icon = icons.batc[step] if charging else icons.bat[step]

    return "{} {}%".format(icon, percent)

def bat():
    return poll(get_bat, 5)
