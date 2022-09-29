#Nicolas Lamback de Paulo
numeros = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
no_rep = list()
maior = 0
for num in numeros:
    if num not in no_rep:
        no_rep.append(num)
for numero in no_rep:
    if numeros.count(numero) > maior:
        maior = numero
print(f'O número que mais se repete é o: {maior}')
