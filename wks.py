from util import async_map, listen

import icons

symbols = {
    'O': icons.wks[2],
    'o': icons.wks[1],
    'F': icons.wks[2],
    'f': icons.wks[0],
    'U': icons.wks[2],
    'u': icons.wks[1],
}

def get_wks(bspc_output):
    items = [item for item in bspc_output.split(':') if item[0] in symbols]
    # out = [symbols[item[0]] for item in items if item[0] in symbols]
    out = [symbols[item[0]].format(item[1:]) for item in items]
    n = len(out)
    if n > 7 and n % 2 == 0:
        out = out[:n//2] + [''] + out[n//2:]
    return ' '.join(out)

def wks():
    return async_map(get_wks, listen('bspc', 'subscribe'))

