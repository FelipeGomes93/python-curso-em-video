'''Faça um programa que tenha uma função chamada contador() que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.'''

def contador(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print(i, end=' ')
    print()
   
#a)
print('-='*20)
print('Contagem de 1 até 10 de 1 em 1: ')
contador(1, 11, 1)

#b)
print('-='*20)
print('Contagem de 10 até 0 de 2 em 2: ')
contador(10, -1, -2)
print('-='*20)

#c)
ini = int(input('Digite o valor inicial da conategem: '))
fi = int(input('Digite o valor final da contagem: '))
pa = int(input('Digite o valor do passo da contagem: '))
print('-='*20)
print('Contagem personalizada: ')
contador(ini, fi, pa)