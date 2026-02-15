'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

num = int(input('Digite um número inteiro: '))
total = soma = 0
menor = maior = num
media = 0
continuar = 'S'
while continuar != 'N':
    total += 1
    soma += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    continuar = input('Deseja continuar? [S/N]:').upper()
    if continuar == 'S':
        num = int(input('Digite um número inteiro: '))
media = soma / total
print('A média entre os valores exibidos é: {:.2f}'.format(media))
print('O maior valor digitado foi {} e o menor valor digitado foi {}'.format(maior, menor))
