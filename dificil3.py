import random
from math import sqrt


def dificil3(n):
    c=0
    for x in range(0, n):
        x0 = random.random()
        y0 = random.random()
        if((sqrt((x0-0.5)**2)+(y0-0.5)**2) < 0.5):
            c+=1
    pi = 4*c/n
    print(pi)
    return pi


if __name__ == '__main__':
    try:
        x = input('Quantidade de simulaçoes  = ')
        z = int(x)
        pi = dificil3(z)
    except:
        print('So numeros inteiros sao aceitos')