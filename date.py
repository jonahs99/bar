from util import poll, execute

def get_date():
    d = execute('date', '+%a %b %d - %H:%M')
    return '{}'.format(d)

def date():
    return poll(get_date, 60)

