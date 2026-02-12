'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

nome = str(input('Digite o seu nome: '))
print('Olá, seja bem vindo(a) {}!'.format(nome))
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
opçao = 0
while opçao != 5:
    print('''Agora, escolha uma das opções abaixo: 
                  [1] somar
                  [2] multiplicar
                  [3] maior
                  [4] novos números
                  [5] sair do programa ''')
    opçao = int(input('Qual é a sua opção: '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
    elif opçao == 2:
        produto = n1 * n2
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, produto))
    elif opçao == 3:
        if n1 > n2:
            print('O maior número é: {}'.format(n1))
        else:
            print('O maior número é: {}'.format(n2))
    elif opçao == 4:
        print('Digite novos números: ')
        n1 = int(input('Digite um número inteiro: '))
        n2 = int(input('Digite outro número inteiro: '))
    elif opçao == 5:
        print('Finalizando....')
    else:
        print('Opção inválida, tente novamente')
print('Fim do programa!')
