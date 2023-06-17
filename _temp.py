print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- Заполните массив элементами арифметической прогрессии.  ---')
print('--- Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.  ---')
print('--- Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.  ---')
print('--- Каждое число вводится с новой строки.  ---')
print('- - - - - - - - - - - - - - - - - - ')
print()
# -I- -----------------------------------------------------

# -F- -------------------------------------------------->->->
def ArithmeticProgressionFor1():
    for i in range(n):
        print(a1 + i * d)

def ArithmeticProgressionRec(a1, d, n):
    if n == 1:
        return [a1]
    else:
        progression = ArithmeticProgressionRec(a1, d, n-1)
        progression.append(a1 + (n-1)*d)
        return progression

def ArithmeticProgressionRecursion():
    while n != 0:
        print(n)
        a1 + (n-1)*d
        n -= 1
        ArithmeticProgressionRecursion()
        print(n)
    return '000'
# -F- -------------------------------------------------<-<-<-

# [ ] -----------------------------------------------------
""" 
a1 = int(input('Введите 1-й элемент: '))
d = int(input('Введите шаг (разность между элементами массива: '))
n = int(input('Введите количество элементов массива: '))
 """
a1, d, n = 1, 2, 4          # 1 3 5 7
# an = 0
# print(a1, d, n)
# ArithmeticProgressionFor1()
""" progression = ArithmeticProgressionRec(a1, d, n)
print(progression) """
ArithmeticProgressionRecursion()
# ArithmeticProgressionRecursion()


# [ ] -----------------------------------------------------
# [ ] -----------------------------------------------------

print()
print('- - - - - - - - - - - - - - - - - - ')


# [--] -1---------------------------------------------------
""" def ArithmeticProgressionRec(a1, d, n):
    if n == 1:
        return [a1]
    else:
        progression = ArithmeticProgressionRec(a1, d, n-1)
        progression.append(a1 + (n-1)*d)
        return progression

progression = ArithmeticProgressionRec(a1, d, n)
print("Ар. прог. 1: ", progression) """
# [--] -2---------------------------------------------------
""" def arithmetic_progression(a1, d, n, progression):
    if n == 0:
        return progression
    else:
        progression.append(a1)
        return arithmetic_progression(a1 + d, d, n - 1, progression)

progression = arithmetic_progression(a1, d, n, [])
print("Ар. прог. 2: ", progression) """
# [--] -3---------------------------------------------------
""" def arithmetic_progression(a1, d, n, progression):
    if n == 0:
        return progression
    else:
        progression.append(a1)
        return arithmetic_progression(a1 + d, d, n - 1, progression)

progression = arithmetic_progression(a1, d, n, [])
for i in range(n):
    print("Ар. прог. 3: ", progression[i]) """

