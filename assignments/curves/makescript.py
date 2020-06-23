def make_script(fname):
    f = open(fname, 'w')

    z = 0
    radius = 1
    while radius < 120:
        f.write('circle\n250 250 {} {}\n'.format(z, radius))
        z += 10
        radius += 4

    f.write('ident\nrotate\ny 50\napply\n')
    f.write('ident\nrotate\nx 45\napply\n')
    f.write('ident\nrotate\nz -60\napply\n')
    f.write('ident\nmove\n-100 350 0\napply\n')
    f.write('display\nsave\npic.png')
    f.close()
