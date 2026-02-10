'''Crie um programa que mostre na tela todos os números pares que estão entre 1 e 50'''

print('Os números pares entre 0 e 50 são: ')
for cont in range(0, 51):
    if cont % 2 == 0:
        print(cont, end =' ')