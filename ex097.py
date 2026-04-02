'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(txt):
    comp = len(txt)  
    print('~'*comp)
    print(txt)
    print('~'*comp)

mensagem = str(input('Digite o texto que deseja exibir: '))
escreva(mensagem)