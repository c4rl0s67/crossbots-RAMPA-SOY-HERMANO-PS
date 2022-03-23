def CrossBots(x):
    if x % 3 == 0 and x % 5 == 0:
        print('"CrossBots"')
        return
    elif x % 5 == 0:
        print('"Bots"')
        return
    elif x % 3 == 0:
        print('"Cross"')
        return
    
    print(x)
    return x


if __name__ == '__main__':
    while True:
        x = input('numero inteiro(x to stop) = ')
        if x == 'x':
            break
        try:
            z = int(x)
            CrossBots(z)
        except:
            print('so numeros inteiros') 
