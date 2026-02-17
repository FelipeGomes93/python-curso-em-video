'''Estatísticas em produtos:
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
'''

total = mais_de_mil = 0
menor_preço = 12000000
nome_menor_preço = ' '

while True:
    print('~='*20)
    print('Loja GOMES')
    print('~='*20)
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    total += preço
    if preço > 1000:
        mais_de_mil += 1
    if preço < menor_preço:
        menor_preço = preço
        nome_menor_preço = nome
    opção = str(input('Deseja continuar a adicionar itens? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break
print('O total da compra é R${:.2f}'.format(total))
print(f'A quantidade de produtos com preço superior a 1000 reais é {mais_de_mil}')
print(f'O produto mais barato é {nome_menor_preço}')