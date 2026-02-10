'''
Crie um programa que faça o computador jogar jokenpô com você
'''
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA ''')
jogador = int(input('Qual a sua jogada: '))
print('-= *' * 20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
elif computador == 1:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
