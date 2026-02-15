'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci'''

n = int(input('Digite o número de termos da sequência de Fibonacci que deseja exibir: '))
primeiro = 0
segundo = 1
cont = 0
while cont < n:
    print(primeiro, end=' ')
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
    cont += 1