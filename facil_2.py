def facil2(x: int):
    b = str(bin(x))
    z = len(b)
    a = 0 
    for y in range(0, z):
        if b[y] == '1':
            a += 1
    print(f'conta_uns({x}) -> {a}')
    return a


if __name__ == '__main__':
    while True:
        x = input('Numero inteiro(x to stop) = ')
        if x == 'x':
            break
        try:
            z = int(x)
            facil2(z)
        except:
            print('Numero deve ser inteiro ') 

