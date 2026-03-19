'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

valores = []
pares = []
impares = []
while True:
    num = (int(input('Digite um valor: ')))
    valores.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar in 'Nn':
        break

print(f'A lista completa é {valores}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
