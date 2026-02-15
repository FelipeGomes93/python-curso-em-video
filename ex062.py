'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mais alguns termos. O programa encerrará quando ele dizer que quer mostrar 0 termos'''

primeiro = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Informe o valor da razão da progressão aritmética: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end =' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))