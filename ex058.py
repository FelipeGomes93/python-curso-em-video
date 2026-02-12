'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
tentativas = 1
computador = randint(0, 10)
jogador = int(input('Digite um número inteiro de 0 a 10: '))
while jogador != computador:
    jogador = int(input('Digite um número inteiro de 0 a 10: '))
    tentativas += 1
print('Foram necessárias {} tentativa para o jogador acertar!'.format(tentativas))

'''from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print('Acertou com {} tentativas. Parabéns!').format(palpites)'''
