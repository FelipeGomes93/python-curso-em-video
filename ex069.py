'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados
C) quantas mulheres tem menos de 20 anos'''

maiores = homens = mulheres_menores_20 = 0

while True:
    print('=-'*20)
    print('CADASTRO')
    print('=-'*20)
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? [M/F]: '))
    if idade > 18:
        maiores +=1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menores_20 += 1
    opção = str(input('Deseja continuar a cadastrar? [S/N]:'))
    if opção in 'Nn':
        break
print(f'A quantidade de pessoas que tem mais de 18 anos é {maiores}')
print(f'A quantidade de homens é {homens}')
print(f'A quantidade de mulheres menores de 20 anos é {mulheres_menores_20}')
