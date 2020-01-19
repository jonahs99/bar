from util import async_map, readline, watch

backlight = '/sys/class/backlight/intel_backlight/'

max_brightness = int(readline(backlight + 'max_brightness'))

def get_bri(line):
    percent = round(int(line) / max_brightness * 100)
    return '{}%'.format(percent)

def bri():
    return async_map(get_bri, watch(backlight + 'brightness'))
