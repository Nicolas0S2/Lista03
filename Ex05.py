#Nicolas Lamback de Paulo
par = 0
impar = 0
for cont in range(1, 11):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'O número de pares foi {par}. E o números de impares foi {impar}.')
