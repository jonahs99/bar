from util import listen, execute
from asyncio import run
from icons import vol_icons, vol_muted_icon

def get_vol():
    percent = int(execute('pamixer', '--get-volume'))
    muted = execute('pamixer', '--get-mute')
    
    if muted == 'false':
        step = percent // 34
        icon = vol_icons[step]
    else:
        icon = vol_muted_icon
    
    return '{} {}%'.format(icon, percent)

async def vol():
    yield get_vol()
    async for line in listen('pactl', 'subscribe'):
        if 'sink #0' not in line:
            continue
        yield get_vol()

