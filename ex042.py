'''
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isosceles: dois lados iguais
- escaleno: todos os lados diferentes
'''
print('~='*20)
print('Analisador de triângulos: ')
print('~='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))


if (r1 < r2 + r3) and (r2 < r1+r3) and (r3 < r1 + r2):
    print('Esses segmentos formam um triângulo')
    if r1 == r2 == r3:
        print('O triângulo formado é EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado é ISÓSCELES')
    else:
        print('O triângulo formado é ESCALENO')
else:
    print('Esses segmentos não formam um triângulo')
    