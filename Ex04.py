#Nicolas Lamback de Paulo
num = int(input('Digite quantas idades: '))
age = 0
for i in range(1, num + 1):
    age += int(input('Digite a idade:'))
print(f'A média das idades digitadas é: {age / num}.')
