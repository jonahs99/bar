import os

def get_colors(file_name):
    colors = []
    file = open(os.path.abspath(file_name))
    for line in file:
        if (i := line.find('#')) != -1:
            colors.append(line[i:i+8])
    return colors

colors = get_colors('.config/colors')

# clr('red bg', 1, 'B') -> '%{Bc[1]}red bg%{B-}'
def clr(txt, i, t='F'):
    return '%{{{}{}}}{}%{{{}-}}'.format(t, colors[i], txt, t)

def und(txt, i):
    return '%{{+uU{}}}{}%{{-uU-}}'.format(colors[i], txt)

left = '%{l}'
center = '%{c}'
right = '%{r}'
