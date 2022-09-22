n = str(input('What is your name?')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu prmeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

