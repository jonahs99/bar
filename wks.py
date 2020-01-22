from util import async_map, listen
import fmt
import icons

def fmt_symbol(s):
    w = ' {} '.format(s[1:])
    link = 'bspc desktop -f {}'.format(s[1:])
    if s[0] in 'FOU':
        w = fmt.und(fmt.clr(w, 15), 2)
    elif s[0] in 'ou':
        w = fmt.clr(w, 15)
    else:
        w = fmt.clr(w, 8)
    return fmt.cmd(w, link)

def get_wks(bspc_output):
    items = [item for item in bspc_output.split(':') if item[0] in 'FOUfou']
    return ''.join(map(fmt_symbol, items))

def wks():
    return async_map(get_wks, listen('bspc', 'subscribe'))

