import math
an = float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(an))
print('O angulo {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O angulo {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O angulo {} tem a TANGENTE de {:.2f}'.format(an, tangente))