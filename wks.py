from util import async_map, listen
import fmt
import icons

def fmt_symbol(s):
    wksname = ' {} '.format(s[1:])
    if s[0] in 'FOU':
        return fmt.und(fmt.clr(wksname, 15), 2)
    elif s[0] in 'ou':
        return fmt.clr(wksname, 15)
    return fmt.clr(wksname, 8)

def get_wks(bspc_output):
    items = [item for item in bspc_output.split(':') if item[0] in 'FOUfou']
    return ''.join(map(fmt_symbol, items))

def wks():
    return async_map(get_wks, listen('bspc', 'subscribe'))

