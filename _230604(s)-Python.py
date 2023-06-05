print()
print('- - - - - - - - - - - - - - - - - - ')

print()
print('- - - - - - - - - - - - - - - - - - ')
print('- - - Простое - - - ')
# |--- -----------------------------------------------------
print()

#  Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

def checkPrime(n, div=2):
    # div- дополнительный параметр для проверки на делимость. При вызове должен быть равен 2 т.к. первое простое число 2
    if n < 2:  # если меьше то не простое
        return False
    elif n == 2:  # если два то сразу простое
        return True
    elif n % div == 0:  # если делится на 2 без остатка сразу выходим - не простое
        return False
    elif (
        div * div > n
    ):  # Проверка что делитель на меньше половины от числа т.к. все что больше половины будет остаток поэтому смысла дальше проверять нет
        return checkPrime(n, div + 1)
    else:
        return True


n = int(input("Введите число: "))
if checkPrime(n):
    print("Простое")
else:
    print("Не простое")

print()
print('- - - - - - - - - - - - - - - - - - ')
print('- - - Палиндром - - - ')
# |--- -----------------------------------------------------
#  введите слово и определите, это палиндром?

# Sergey Antipov
def pal(word):
    if len(word) == 0: return ''
    c = word.pop(0)
    return pal(word) + c

print()
print('- - - - - - - - - - - - - - - - - - ')
word = 'око'
text = [item for item in word]
if word == pal(text): print('Да')
else: print('Нет')

print()
print('- - - - - - - - - - - - - - - - - - ')
def poli(s):
    if len(s) in [1,2]:
        return s[0] == s[-1]
    return s[0] == s[-1] and poli(s[1:len(s)-1])

a = "abccba"
print(poli(a))

print()
print('- - - - - - - - - - - - - - - - - - ')

""" Сергей Сердюк
if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
            print(*list_1[i]) """


""" Сергей Сердюк
n = int(input())
list_1 = list()
for i in range(n):
    summa = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            summa += j
    list_1.append(tuple([i, summa]))
for i in range(len(list_1)):
    for j in range(i, len(list_1)):
        if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
            print(*list_1[i]) """


""" Виталий Шалай
from random import randint

n = 20
list = []
for i in range(n):
    list.append(randint(1,10))
print(list)
counter = 0
for i  in range(1, n - 1):
    if list[i-1] < list[i] > list[i+1]:
        counter +=1
        print(f"{list[i]} - [{i}],", end=' ')
print(f' :[{counter}]') """


""" Дмитрий Пешков
def s(n):
    list1 = [i for i in range(1,n) if n % i == 0]
    sum = 0
    for i in list1:
        sum += i
        # print(i)
    return sum    
    
k = 300
for i in range(1,k):
    for j in range(1,k):
        if s(i) == j and s(j) == i and i != j:
            print(f"{i} и {j}") """

print('- - - - - - - - - - - - - - - - - - ')


