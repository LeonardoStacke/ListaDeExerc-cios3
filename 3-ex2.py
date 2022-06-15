lista = []
multis = []
for i in range(5):
    n = int(input('Digite um número: '))
    lista.append(n)
    multis.append(n)
    if i>=1:
        mult = n*multis[0]
        multis.insert(0,mult)
soma = sum(lista)
print('Soma: ',soma)
print('Multiplicação: ',multis[0])
print('Números: ',lista)