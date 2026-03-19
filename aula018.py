teste = list()
teste.append('Felipe')
teste.append(33)
galera = list()
galera.append(teste[:])
teste[0] = 'Andreia'
teste[1] = 32
galera.append(teste[:])
print(galera)
