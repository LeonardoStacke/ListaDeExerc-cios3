vetor = []
quad = []

for i in range(1,11):
    n = int(input('Digite o {}º número: '.format(i)))
    vetor.append(n)
    q = n**2
    quad.append(q)
soma = sum(quad)
print('A soma é: ',soma)