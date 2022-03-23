def criar_matriz(n):
    matriz = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
    for i in range(n):
        linha = []
        for j in range(n):
            x = input(f'Valor de M[{i+1}][{j+1}] = ')
            linha.append(x)
            if j == n-1:
                linha.append('X')
        matriz.append(linha)
    matriz.append(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'])
    return matriz


def dificil1(m, n):
    linha = 0
    coluna = 1
    acoes = ['X']
    indice = 0
    c = 0
    k = True
    limite = 0  
    while k:
        if coluna == n and linha == n - 1:
            k = False
            break
        if m[coluna + 1][linha] == 'M' and acoes[indice] != 'up':
            coluna += 1
            acoes.append('down')
            indice = len(acoes) - 1
            c += 1
            limite += 1
            pass
        elif m[coluna][linha + 1] == 'M' and acoes[indice] != 'left':
            linha += 1
            acoes.append('rigth')
            indice = len(acoes) - 1
            c += 1
            limite += 1
            pass
        elif m[coluna - 1][linha] == 'M' and acoes[indice] != 'down':
            coluna -= 1
            acoes.append('up')
            indice = len(acoes) - 1
            c += 1
            limite += 1
            pass
        elif m[coluna][linha - 1] == 'M' and acoes[indice] != 'rigth':
            linha -= 1
            acoes.append('left')
            indice = len(acoes) - 1
            c += 1
            limite += 1
            pass
        if limite == 1000:
            c = 'SI'
            k = False

    print(f'Movimentos necessario = {c}')   
    return c

     
if __name__ == "__main__":
    n = input('Digite o valor de n = ')
    try:
        x = int(n)
        if x >= 4 and x <= 7:
            matriz = criar_matriz(x)
        else:
            print('N deve ser um numero inteiro de 4 a 7')
    except:
        print('N deve ser um numero inteiro de 4 a 7')
    
    resposta = dificil1(matriz, x)
  
    