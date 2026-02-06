'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))

media = (nota_1 + nota_2) / 2

if media < 5.0:
    print('A nota final do aluno é {:.1f} e seu resultado é: REPROVADO'.format(media))
elif media >= 5.0 and media <=6.9:
     print('A nota final do aluno é {:.1f} e seu resultado é: RECUPERAÇÃO'.format(media))
elif media >= 7.0:
      print('A nota final do aluno é {:.1f} e seu resultado é: APROVADO'.format(media))