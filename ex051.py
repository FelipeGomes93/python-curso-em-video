'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão'''

primeiro = int(input('Digite o primeiro termo da sequência: '))
razao = int(input('Digite a razão da progressão aritmética: '))
for cont in range(primeiro,11, razao):
    print('{}'.format(cont), end=' ')
print('ACABOU')