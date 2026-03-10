'''
- listas são mutáveis, ao contrário das tuplas;
- listas são representadas por colchetes;
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
- para adicionar um item a lista:
    lanche.append('cookie')
- lanche.insert(0, 'cachorro quente')
- para apagar elementos:
    - del lanche[3]
    - lanche.pop(3)
    - lanche.remove('pizza')
- valores = list(range(4, 11))
- para ordenar valores:
    - valores = [8, 2, 5, 4, 9, 3, 0]
    - valores.sort()
    - 0, 2, 3, 4, 5, 8, 9
    - valores.sort(reverse=True)
'''
#==========================================

'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.insert(2, 0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

#==========================================

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')'''

#==========================================

'''valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')'''

#==========================================
