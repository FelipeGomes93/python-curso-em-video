'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 25 anos: sênior
- acima: master
'''

ano_nascimento = int(input('Qual o ano de nascimento do atleta: '))
idade = 2026 - ano_nascimento
if idade <= 9:
    print('O atleta tem {} anos e é da categoria: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e é da categoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e é da categoria: JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e é da categoria: SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos e é da categoria: MASTER'.format(idade))   