'''Crie um programa que leia vários númeos inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles'''

n = s = qtd = 0

while True:
    n = int(input('Digite um número inteiro: (999 para parar) '))
    if n == 999:
        break
    s += n
    qtd += 1
print(f'A soma dos números foi {s} e a quantidade de números digitados foi {qtd}')