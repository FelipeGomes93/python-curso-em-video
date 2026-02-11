'''Detector de palíndromo:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1,-1,-1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo')