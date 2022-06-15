n = []
acima = []

for i in range(1,5):
    notas = []
    nome = (input('Nome do aluno {}: '.format(i)))
    n.append(nome)

    for j in range(1,5):
        nota = float(input('Nota {} do aluno {}: '.format(j, nome)))
        notas.append(nota)
    media1 = sum(notas)/4
    n.append(media1)

    if media1>=7:
        acima.append(nome)
        acima.append(media1)

print(*acima, sep = ',')

