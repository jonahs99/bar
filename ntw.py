from util import async_map, execute, listen
import icons

symbols = {
    'disconnected': icons.ntw[0],
    'connecting': icons.ntw[1],
    'connected (local only)': icons.ntw[1],
    'connected (site only)': icons.ntw[1],
    'connected': icons.ntw[2],
}

def get_ntw(_):
    state, connectivity, _, _, _, _ = execute('nmcli', '-t', 'g').split(':')
    network = execute('nmcli', '-t', '-f', 'NAME', 'c', 'show', '--active')

    symbol = symbols[state if state in symbols else 'disconnected']
    return '{} {}'.format(symbol, network)

def ntw():
    return async_map(get_ntw, listen('nmcli', 'm', immediate=True))
