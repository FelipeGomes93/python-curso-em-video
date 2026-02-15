'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuári digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles'''

num = int(input('Digite um número inteiro: '))
total = 0
soma = 0
while num != 999:
    total +=1
    soma += num
    num = int(input('Digite um número inteiro (999 para sair): '))
print('O total de números digitados foi: {}'.format(total))
print('A soma total dos valores digitados foi: {}'.format(soma))
