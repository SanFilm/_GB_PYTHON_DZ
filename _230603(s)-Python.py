print()
print('- - - - - - - - - - - - - - - - - - ')

# sum = inputArray1[i - 2] + inputArray1[i - 1] + inputArray1[i]

print('- - - - - - - - - - - - - - - - - - ')
print()
print('- - - Последовательность Фибоначчи - - - ')
print()

""" 
10:25
Задача No31. Решение в группах
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
Input: 7 Output: 21
Задание необходимо решать через рекурсию """

# [ ]- Фибоначчи - Рекурсия ------------------------------------------------------
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# ! >->->- https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number/ >->->-

# Function for nth Fibonacci number
# Функция для n-го числа Фибоначчи
def Fibonacci(n):
    if n<= 0:
        print("Неправильный ввод")
    # First Fibonacci number is 0
    # Первое число Фибоначчи равно 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    # Второе число Фибоначчи равно 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
# Driver Program
print(Fibonacci(10))

# ! <-<-<- https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number/ <-<-<-

print()
print('- - - Факториал числа - - - ')
print()

""" Сергей Сердюк
факториал числа найти. вводите число и находите рекурсией его факториал. для 5 факториал 120 """

""" def factorial(n):
    if n < 1:   # base case
        return 1
    else:
        returnNumber = n * factorial(n - 1)  # recursive call
        print(str(n) + '! = ' + str(returnNumber))
        return returnNumber """
# [ ]- While ------------------------------------------------------
n = int(input())
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)
# [ ]- For ------------------------------------------------------
n = int(input())
factorial = 1
for i in range(2, n+1):
    factorial *= i
print(factorial)
# [ ]- Рекурсия ------------------------------------------------------
def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n
print(fac(5))
# [ ]-  ------------------------------------------------------
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return (n * factorial(n-1))
n = int(input("Введите число: "))
print("Факториал числа равен: ")
print(factorial(n))

print('- - - - - - - - - - - - - - - - - - ')
print('- - -  - - - ')

""" Сергей Сердюк
Задача No35. Решение в группах
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5 Output: yes """
print('- - - - - - - - - - - - - - - - - - ')

print('- - - Палиндром - - - ')

# Sergey Antipov
def pal(word):
    if len(word) == 0: return ''
    c = word.pop(0)
    return pal(word) + c

word = 'окно'
text = [item for item in word]
if word == pal(text): print('Да')
else: print('Нет')

print()
print('- - - - - - - - - - - - - - - - - - ')


