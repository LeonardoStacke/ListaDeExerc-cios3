def funcao(l, c):
    if l > 20:
        l = 20
    elif l < 1:
        l = 1

    if c > 20:
        c = 20
    elif c < 1:
        c = 1

    for x in range(l):
        if x == 0 or x == l - 1:
            print('+' + ('-' * (c - 2)) + '+')
        else:
            print('|' + ('-' * (c - 2)) + '|')
    return ''


l = int(input('Número de linhas: '))
c = int(input('Número de colunas: '))

print(funcao(l, c))
