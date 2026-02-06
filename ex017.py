'''co = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {}'.format(hip))'''

import math
co = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {}'.format(hi))