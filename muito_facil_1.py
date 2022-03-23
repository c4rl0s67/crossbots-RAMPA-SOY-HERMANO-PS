from math import pi


def muito_facil1(x: float):
    y = round(180*x/pi, 1)
    print(f'radianos_graus({x})-> {y} graus')
    return y


if __name__ == '__main__':
    while True:
        x = input('Angulo em radianos(x to stop) = ')
        if x == 'x':
            break
        try:
            z = float(x)
            muito_facil1(z)

        except:
            print('X deve ser um numero inteiro ou float')
            


    
