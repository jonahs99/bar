from util import async_map, execute, listen
import fmt
import icons

symbols = {
    'disconnected': fmt.clr(icons.ntw[0], 1),
    'connecting': fmt.clr(icons.ntw[1], 3),
    'connected (local only)': fmt.clr(icons.ntw[1], 11),
    'connected (site only)': fmt.clr(icons.ntw[1], 11),
    'connected': icons.ntw[2]
}

def get_ntw(_):
    state, connectivity, _, _, _, _ = execute('nmcli', '-t', 'g').split(':')
    network = execute('nmcli', '-t', '-f', 'NAME', 'c', 'show', '--active')

    symbol = symbols[state if state in symbols else 'disconnected']
    return '{} {}'.format(symbol, network)

def ntw():
    return async_map(get_ntw, listen('nmcli', 'm', immediate=True))
