#Nicolas Lamback de Paulo
numero = int(input('Digite um número inteiro positivo: '))
print('Esses são seus divisores:')
for num in range(1, numero + 1):
    if numero % num == 0:
        print(num, end= ' ')
