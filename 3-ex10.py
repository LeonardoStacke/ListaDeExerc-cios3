matriz = [[0,0,0],[0,0,0],[0,0,0]]
k = int(input('Digite o valor do multiplicador: '))

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input('Digite os valores [{}][{}] '.format(i,j)))

print('-'*30)

print('Antes da multiplicação:')

for i in range(3):
    for j in range(3):
        print('[{:^5}]'.format(matriz[i][j]), end='')
    print()
print('-'*30)


print('Depois da multiplicação:')

for i in range(3):
    for j in range(3):
        if i == j:
            matriz[i][j] = matriz[i][j] * k
        print('[{:^5}]'.format(matriz[i][j]), end='')
    print()
print('-'*30)