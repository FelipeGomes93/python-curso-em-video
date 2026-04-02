'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(l,c):
    a = l*c
    print(f'A área do terreno com largura {l}m e comprimento {c}m é de {a}m².')

l = float(input('Digite o valor da medida da largura do terreno: '))
c = float(input('Digite o valor da medida do comprimento do terreno: '))

area(l,c)