print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- Петя помогает Кате по математике. ---')
print('--- Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. ---')
print('--- Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. ---')
print('--- Помогите Кате отгадать задуманные Петей числа. ---')
print('- - - - - - - - - - - - - - - - - - ')
print()

""" s = int(input('Задай сумму двух чисел \n'))
p = int(input('Задай произведение чисел \n'))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'первое число ="{x}", второе число ="{y}"') """

print('Введите 2 числа через пробел:')
a, b = map(int, input().split())
res = []
for i in range(a + b):
    if i == (a * i - b)**0.5:
        res.append(i)
print(*res if len(res) == 2 else res + res)

print()
print('- - - - - - - - - - - - - - - - - - ')
print()

x = int(input('Ведите 1-е число: '))
y = int(input('Ведите 2-е число: '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)

print()
print('- - - - - - - - - - - - - - - - - - ')
