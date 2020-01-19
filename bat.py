from util import readline, poll
import icons

online = '/sys/class/power_supply/AC/online'
bat0 = '/sys/class/power_supply/BAT0/'

energy_full = int(readline(bat0 + 'energy_full'))

def get_bat():
    charging = int(readline(online))
    percent = round(float(readline(bat0 + 'energy_now')) / energy_full * 100)
    step = percent // 10

    icon = icons.batc[step] if charging else icons.bat[step]

    return '{} {}%'.format(icon, percent)

def bat():
    return poll(get_bat)

