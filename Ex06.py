#Nicolas Lamback de Paulo
esta = 0
nao_esta = 0
for numero in range(1, 11):
    num = int(input('Digite um número: '))
    if num >= 10 and num <= 20:
        esta += 1
    else:
        nao_esta += 1
print(f'{esta} dos números digitados estão entre 10 e 20. E {nao_esta} dos números digitados não estão entre 10 e 20.')
