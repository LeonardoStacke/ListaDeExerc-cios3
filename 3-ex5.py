vetorA = []
vetorB = []
vetorC = []

for i in range(1,11):
    nome = str(input('Digite o {}º nome de A: '.format(i)))
    vetorA.append(nome)
print('-'*20)
for i in range(1,11):
    nome = str(input('Digite o {}º nome de B: '.format(i)))
    vetorB.append(nome)
print('-' * 20)
for i in range(10):
    print(vetorA[i])
    print(vetorB[i])
    print('-'*10)