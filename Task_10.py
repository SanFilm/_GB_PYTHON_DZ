print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- На столе лежат \'n\' монеток.  ---')
print('--- Определите минимальное число монеток, которые нужно перевернуть, ---')
print('--- чтобы все монетки были повернуты вверх одной стороной. ---')
print('--- Выведите минимальное количество монет, которые нужно перевернуть. ---')
print('- - - - - - - - - - - - - - - - - - ')
print()

# -I- -----------------------------------------------------
import random

# -F- -------------------------------------------------->->->
def RandomNumbers():
    n = int(input('Введите количество элементов списка: '))
    min, max = 0, 1
    for i in range(n):
        number = random.randint(min, max)
        coins.append(number)

def LowestValue():
    c0 = c1 = 0
    for i in coins:
        if i == 0:
            c0 += 1
        else:
            c1 += 1
    if c0 < c1:
        print(f'Минимальное количество монет, которые нужно перевернуть: {c0}')
    else:
        print(f'Минимальное количество монет, которые нужно перевернуть: {c1}')
# -F- -------------------------------------------------<-<-<-

# [ ] -----------------------------------------------------
coins = []
RandomNumbers()
print(coins)
LowestValue()
# [ ] -----------------------------------------------------
print()
print('- - - - - - - - - - - - - - - - - - ')
