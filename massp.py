import genCard
import time

ha = open('cards.txt', 'a+')
sp = '    '

for i in range(100000):
    pin = genCard.genpin()
    serial = genCard.genserial()
    card = pin + sp + serial + '\n'
    ha.write(card)
    time.sleep(1.5)
    print(i+1)

