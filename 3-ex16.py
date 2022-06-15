def somaImposto(taxaImposto,custo):

    soma = custo*(taxaImposto*0.01+1)
    return soma

custo = float(input('Custo do produto: '))
taxaImposto = float(input('Imposto em %: '))

print('=-'*15)

print('O total do valor é: ', somaImposto(taxaImposto, custo))