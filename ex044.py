'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista, dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

preço = float(input('Digite o valor do produto: '))
opção = int(input('''Escolha uma das opções de pagamento:
      1 - à vista, dinheiro/cheque
      2 - à vista no cartão
      3 - em até 2x no cartão
      4 - 3x ou mais no cartão '''))

if opção == 1:
    print('O valor a ser pago pelo produto é: {:.2f}'.format(preço*0.9))
elif opção == 2:
    print('O valor a ser pago pelo produto é: {:.2f}'.format(preço*0.95))
elif opção == 3:
    print('O valor a ser pago pelo produto é: {:.2f}'.format(preço))
elif opção == 4:
    print('O valor a ser pago pelo produto é: {:.2f}'.format(preço*1.2))
else:
    print('Opção inválida, tente novamente')