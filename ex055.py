'''Maior e menor sequência:
Faça um programa que leia o peso de cinco pessoas . No final, mostre qual foi o maior e o menor peso lidos'''
maior = 0
menor = 500
for c in range(1,6):
    peso = int(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso registrado foi {}kg e o menor peso registrado foi {}kg'.format(maior, menor))