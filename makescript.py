def make_script(fname):
    f = open(fname, 'w')
    f.write('ident\n')
    x = 0
    y = 0
    while x <= 1000:
        f.write('sphere\n{} {} 0 50\n'.format(x, y))
        x += 100
        y += 25
    x = 0
    while x <= 1000:
        f.write('torus\n{} 250 0 10 75\n'.format(x))
        x += 175
    f.write('rotate\nz 20\nrotate\nx 20\nrotate\ny 20\n')
    f.write('apply\ndisplay\nsave\npic.png')
    f.close()
