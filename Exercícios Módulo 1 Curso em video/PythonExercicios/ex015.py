dias = int(input('Quantos dias de aluguel?'))
km = float(input('Quantos Km rodados?'))
pago = (dias * 60.00) + (km * 0.15)
print('O total a pagar é de R${:.2f}:'.format(pago))