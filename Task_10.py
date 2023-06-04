print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- На столе лежат \'n\' монеток.  ---')
print('--- Определите минимальное число монеток, которые нужно перевернуть, ---')
print('--- чтобы все монетки были повернуты вверх одной стороной. ---')
print('--- Выведите минимальное количество монет, которые нужно перевернуть. ---')
print('- - - - - - - - - - - - - - - - - - ')
print()
# n = int(input('Введите ширину плитки n: '))

""" import random
def RandomNumbers():
    # n = int(input('Введите ширину плитки n: '))
    print("Введите два числа, минимальное и максимальное")
    min = int(input("Введите min. "))
    max = int(input("Введите max. "))

    for i in range(10):
        number = random.randint(min, max)
        print(str(number)+ str(" "), end="")

RandomNumbers() """
# print()
coins = [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
print(coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))


print()
