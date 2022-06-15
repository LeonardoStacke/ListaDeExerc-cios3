st1 = str(input('Frase 1: '))
st2 = str(input('Frase 2: '))
t1 = len(st1)
t2 = len(st2)

print('String 1: "{}"'.format(st1))
print('String 2: "{}"'.format(st2))
print('Tamanho da String 1: {} caracteres'.format(t1))
print('Tamanho da String 2: {} caracteres'.format(t2))

print('-'*30)

if t1==t2:
    print('Elas possuem tamanhos iguais.')
else:
    print('Elas possuem tamanhos diferentes.')
print('-'*30)
if st1==st2:
    print('Elas possuem o mesmo conteúdo.')
else:
    print('Elas possuem conteúdos diferentes.')
print('-'*30)