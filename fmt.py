import os

colors = [ os.environ['color' + str(i)] for i in range(16) ]

# Usage: clr('red bg', 1, 'B') -> '%{B$color1}red bg%{B-}'
def clr(txt, i, t='F'):
    return '%{{{}{}}}{}%{{{}-}}'.format(t, colors[i], txt, t)

# Usage: und('blue underline', 4) -> '%{+uU$color4}blue underline%{-uU-}'
def und(txt, i):
    return '%{{+uU{}}}{}%{{-uU-}}'.format(colors[i], txt)

# Run something 
def cmd(txt, command, button=1):
    return '%{{A:{}:}}{}%{{A}}'.format(command, txt)

left = '%{l}'
center = '%{c}'
right = '%{r}'
