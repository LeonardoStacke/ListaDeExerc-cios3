matriz1 = [[0,0,0],[0,0,0]]
matriz2 = [[0,0,0],[0,0,0]]
matriz3 = [[0,0,0],[0,0,0]]

for i in range(2):
    for j in range(2):
        matriz1[i][j] = int(input('Digite o valor [{}][{}] de A: '.format(i,j)))

for i in range(2):
    for j in range(2):
        matriz2[i][j] = int(input('Digite o valor [{}][{}] de B: '.format(i,j)))

for i in range(2):
    for j in range(2):
        matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
        print('[{:^3}]'.format(matriz3[i][j]), end='')
    print()