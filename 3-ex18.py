import sys

def data(dia, mes, ano):
    if (mes == 2 or 4 or 5 or 6 or 9 or 11):
        if dia > 31:
            print('NULL: Data inválida')
            sys.exit()

    elif dia > 31:
        print('NULL: Data inválida')
        sys.exit()

    if mes == 1:
            mes = str('Janeiro')
    elif mes == 2:
            mes = str('Fevereiro')
    elif mes == 3:
            mes = str('Março')
    elif mes == 4:
            mes = str('Abril')
    elif mes == 5:
            mes = str('Maio')
    elif mes == 6:
            mes = str('Junho')
    elif mes == 7:
            mes = str('Julho')
    elif mes == 8:
            mes = str('Agosto')
    elif mes == 9:
            mes = str('Setembro')
    elif mes == 10:
            mes = str('Outubro')
    elif mes == 11:
            mes = str('Novembro')
    elif mes == 12:
            mes = str('Dezembro')
    else:
        print('NULL: Data inválida')
        sys.exit()

    return '{} de {} de {}'.format(dia, mes, ano)


dias, meses, anos = input('Digite a data (DD/MM/AAAA): ').split('/')
dia=int(dias)
mes=int(meses)
ano=int(anos)

print('=-'*20)
print(data(dia, mes, ano))
