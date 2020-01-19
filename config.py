from wks import wks
from bat import bat
from bri import bri
from date import date
from vol import vol

left = '%{l}'
center = '%{c}'
right = '%{r}'

bar = [
    left, ' ', wks(),
    center, date(),
    right, bri(), '  ', vol(), '  ', bat(), ' ',
]

