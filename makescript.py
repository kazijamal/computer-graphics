def make_script(fname):
    f = open(fname, 'w')

    x1 = 0
    x2 = 25
    x3 = 50
    
    while x3 <= 1000:
        z1 = -1000
        z2 = -975
        z3 = -950
        while z3 <= 1000:
            f.write('line\n{} 0 {} {} 0 {}\n'.format(x1, z1, x2, z1))
            f.write('line\n{} 0 {} {} 25 {}\n'.format(x2, z1, x2, z1))
            f.write('line\n{} 25 {} {} 25 {}\n'.format(x2, z1, x1, z1))
            f.write('line\n{} 25 {} {} 0 {}\n'.format(x1, z1, x1, z1))
            f.write('line\n{} 0 {} {} 0 {}\n'.format(x1, z2, x2, z2))
            f.write('line\n{} 0 {} {} 25 {}\n'.format(x2, z2, x2, z2))
            f.write('line\n{} 25 {} {} 25 {}\n'.format(x2, z2, x1, z2))
            f.write('line\n{} 25 {} {} 0 {}\n'.format(x1, z2, x1, z2))
            f.write('line\n{} 0 {} {} 0 {}\n'.format(x1, z1, x1, z2))
            f.write('line\n{} 25 {} {} 25 {}\n'.format(x1, z1, x1, z2))
            f.write('line\n{} 25 {} {} 25 {}\n'.format(x2, z1, x2, z2))
            f.write('line\n{} 0 {} {} 0 {}\n'.format(x2, z1, x2, z2))
            z1 += 50
            z2 += 50
            z3 += 50
        x1 += 50
        x2 += 50
        x3 += 50

    f.write('rotate\nz 20\nrotate\nx 20\nrotate\ny 20\n')
    f.write('apply\nident\nrotate\ny 20\napply\ndisplay\n')
    f.close()
