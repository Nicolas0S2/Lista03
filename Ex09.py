#Nicolas Lamback de Paulo
numeros = list()
for num in range(1, 11):
    usuario = int(input('Digite um número: '))
    numeros.append(usuario)
numeros.sort()
print('Números em ordem crescente:')
print(numeros)
