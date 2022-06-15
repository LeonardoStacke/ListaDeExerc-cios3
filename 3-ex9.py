nome = str(input('Digite seu nome: ')).upper()
n=""
nome.upper()
for i in range(len(nome)):
    print('{}{}'.format(n, nome[i]))
    nomes = nome[i]
    n = n+ nomes
