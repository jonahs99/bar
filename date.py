from util import poll, execute

def get_date():
    d = execute('date', '+%H:%M  %b %d %Y')
    return '{}'.format(d)

def date():
    return poll(get_date, 60)

