preço = float(input('O preço do produto é: R$'))
novo = preço - (preço * 5 / 100)
print('O preço do produto é R${:.2f}, com desconto de 5% fica em R${:.2f}'.format(preço, novo))
