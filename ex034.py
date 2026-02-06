'''
Escreva um rpograma que pergunte o salaário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
'''

salario = float(input('Digite o salário do funcionário: '))
if salario <= 1250:
    salario_novo = salario * 1.15
else:
    salario_novo = salario * 1.10

print('Quem recebia R${:.2f}, agora recebe R${:.2f}'.format(salario, salario_novo))