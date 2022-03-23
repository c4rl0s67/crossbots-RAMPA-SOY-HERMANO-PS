def muito_facil2(x):
    m = x / 720
    s = x / 168
    d = x / 24
    y = x * 60
    z = x * 3600
    w = x * 3600000
    resposta = f"""[{m:.0f},{s:.0f},{d:.0f},{x},{y},{z},{w}]"""
    print(f'Converter({x}) -> [meses={m:.0f},semanas={s:.0f},dias={d:.0f},horas={x},min={y},seg={z},miliseg= {w}]')
    return resposta

if __name__ == '__main__':
    while True:
        x = input('Valor em horas(x to stop) = ')
        if x == 'x':
            break
        try:
            z = int(x)
            muito_facil2(z)
        except:
            print('X deve ser um numero inteiro ou float')