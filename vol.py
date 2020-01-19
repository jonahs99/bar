from util import async_map, listen, execute
from asyncio import run
import icons

def get_vol(line):
    if 'sink #0' not in line:
        return None

    percent = int(execute('pamixer', '--get-volume'))
    muted = execute('pamixer', '--get-mute')
    
    if muted == 'false':
        step = percent // 34
        icon = icons.vol[step]
    else:
        icon = icons.vol_muted
    
    return '{} {}%'.format(icon, percent)

def vol():
    return async_map(get_vol, listen('pactl', 'subscribe', immediate='sink #0'))

