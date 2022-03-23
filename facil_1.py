def facil1(x: str, n: int):
    w = []
    for y in range(0, n):
        w.append(x)
    print(f'repeti("{x}", {n}) -> {w}')
    return w


if __name__ == '__main__':
    while True:
        x = input('item(x to stop) = ')
        if x == 'x':
            break
        y = input('N(x to stop) = ')
        if y == 'x':
            break
        try:
            z = int(y)
            facil1(x, z)
        except:
            print('Item deve ser uma str e n um numero inteiro ')    
   
    
