'''Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) quantas pessoas foram cadastradas
B) uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves'''

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram: {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg.')
print(f'O menor peso foi de {men}Kg.')
