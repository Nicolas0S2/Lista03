#Nicolas Lamback de Paulo
inteiro = int(input('Digite um número inteiro de 1 a 10: '))
while inteiro > 10:
    print('Opção inválida! tente novamente.')
    inteiro = int(input('Digite um número inteiro de 1 a 10: '))
for num in range(1, 11):
    print(f'{num} x {inteiro} == {num * inteiro}')
