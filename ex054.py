'''Grupo da maioridade:
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''
maiores = 0
menores = 0
for c in range(1,8):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    if (2026 - ano_nascimento) >= 18:
        maiores += 1
    else:
        menores += 1
print('{} pessoas são maiores de idade e {} pessoas são menores de idade'.format(maiores, menores))