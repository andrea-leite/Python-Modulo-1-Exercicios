from random import randint
from time import sleep
computador = randint(0,5)
print('-=-'* 20)
print('VOu pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'* 20)
print('Processando...')
sleep(2)
jogador = int(input('Em que número eu pensei?'))#jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))

