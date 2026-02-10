'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- acima de 40: Obesidade mórbida
'''

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / altura**2
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no peso ideal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você esta com obesidade')
else:
    print('Você está com obesidade mórbida')