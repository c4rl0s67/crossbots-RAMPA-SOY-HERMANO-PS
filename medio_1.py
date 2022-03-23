from cmath import sqrt


def medio1(x0, y0, x1, y1):
    d = sqrt(((x0 - x1)**2) + (y0 - y1)**2)
    print(f'Distancia(({x0},{y0}), ({x1}, {y1})) -> {d}')
    return d


if __name__ == '__main__':
    while True:
        x = input('X0(x to stop) = ')
        if x == 'x':
            break
        y = input('Y0(x to stop) = ')
        if y == 'x':
            break
        xx = input('X1(x to stop) = ')
        if x == 'x':
            break
        yy = input('Y2(x to stop) = ')
        if y == 'x':
            break
        try:
            x0 = float(x)
            y0 = float(y)
            x1 = float(xx)
            y1 = float(yy)
            medio1(x0, y0, x1, y1)
        except:
            print('Todos os valores devem ser numericos ') 
