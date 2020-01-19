from util import listen, execute
from asyncio import run
import icons

def get_vol():
    percent = int(execute('pamixer', '--get-volume'))
    muted = execute('pamixer', '--get-mute')
    
    if muted == 'false':
        step = percent // 34
        icon = icons.vol[step]
    else:
        icon = icons.vol_muted
    
    return '{} {}%'.format(icon, percent)

async def vol():
    yield get_vol()
    async for line in listen('pactl', 'subscribe'):
        if 'sink #0' not in line:
            continue
        yield get_vol()

