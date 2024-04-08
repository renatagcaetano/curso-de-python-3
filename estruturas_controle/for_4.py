'''
for i in range(1, 11):
    print(i)
else:
    print('Fim!')

for j in range(1, 11):
    if j == 6:
        break
    print(j)
else:
    print('Fim!')
'''
from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 != 0:
        continue
    
    if i == sortear_dado():
        print('ACERTOU', i)
        break
else:
    print('Não acertou o número.')
