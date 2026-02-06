'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = 2026 - ano_nascimento
if idade < 18:
    print('Em 2026 você tem {} anos, ainda faltam {} anos para você se alistar'.format(idade, 18-idade))
elif idade == 18:
    print('Em 2026 você tem {} anos, está na hora de se alistar.'.format(idade))
elif idade > 18:
    print('Em 2026 você tem {} anos. Já passou o tempo do seu alistamento em {} anos'.format(idade, idade-18))