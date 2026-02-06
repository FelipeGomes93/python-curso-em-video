km = int(input('Digite a quantidade de km rodados: '))
dias = int(input('Digite a quantidade de dias utilizados: '))
preco = float(km*0.15 + dias*60)
print('O preço a ser pago pelo aluguel do carro é R${:.2f}' .format(preco))