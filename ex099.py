'''Faça um programa que tenha uma função chamada maior(), que recebe vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''

def maior(* valores):
    print('-='*20)
    print('Analisando os valores passados...')
    maior = 0
    for v in valores:
        print(v, end=' ')
        if v == valores[0]:
            maior = v
        elif v > maior:
            maior = v

    print(f'\nO maior valor foi {maior}')

maior(2, 9, 4, 5, 7, 1)
