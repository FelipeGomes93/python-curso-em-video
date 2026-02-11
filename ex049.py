'''Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher. Só que agora, utilizando o laço for'''

num = int(input('Digite o número do qual deseja exibir a tabuada: '))
for cont in range(1,11):
    print('{} x {} = {}'.format(num, cont, num*cont))