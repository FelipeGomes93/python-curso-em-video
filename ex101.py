'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com idade {idade} anos: NEGADO'
    elif 16<= idade < 18 or idade > 65:
        return f'Com idade {idade} anos: OPCIONAL'
    else:
        return f'Com idade {idade} anos: OBRIGATÓRIO'

#programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))