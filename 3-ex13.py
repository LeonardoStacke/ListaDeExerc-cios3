n = int(input('Digite um número: '))
lista=[]
a =1

for i in range(n+1):
    if i==0:
        lista.append(0)
    else:
        lista.append(i)

for i in range(1,n+1,1):
    if i==1:
        print(i)
    else:
        print('{}{}'.format(a, lista[i]))
        x=lista[i]
        a = f'{a}'+f'{x}'

