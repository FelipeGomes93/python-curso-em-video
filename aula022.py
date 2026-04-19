'''Modularização
- Surgiu na década de 60;
- Sistemas ficando cada vez maiores;
- Foco: dividir um programa grande;
- Foco: aumentar a legibilidade;
- Foco: facilitar a manutenção.'''

from uteis import numeros

num = int(input("Digite um número inteiro: "))
fat = numeros.fatorial(num)
dob = numeros.dobro(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dob}')
