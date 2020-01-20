from wks import wks
from title import title
from bat import bat
from bri import bri
from date import date
from vol import vol
from ntw import ntw

from fmt import left, center, right

bar = [
    left, wks(), ' ', title(),
    center, date(),
    right, ntw(), '  ', bri(), '  ', vol(), '  ', bat(), ' ',
]

