lista=[]

for p in range(1,6):
    nome = str(input('Nome da pessoa {}: '.format(p)))
    idade = int(input('Idade do {}: '.format(nome)))
    altura = float(input('Altura do {}: '.format(nome)))
    lista.append(altura)
    lista.append(idade)
    lista.append(nome)

for i in range(14,-1,-3):
    print('Nome: ', lista[i])
    print('Idade: ', lista[i-1])
    print('Altura: ', lista[i-2])
    print('-'*20)