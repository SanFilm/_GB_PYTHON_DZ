print()
print('- - - - - - - - - - - - - - - - - - ')
# Таск_16

# Таск_18

""" n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

k = int(input())
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number) """


""" 
# Алексей Минченя
# Задача №18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
from random import randint

N = int(input("Введите число N: "))
inputList = [randint(1, N) for i in range(N)]
print(inputList)
X = int(input("Введите число X: "))

diffP = 0
oldDiffP = max(inputList)
diffN = 0
oldDiffN = max(inputList)
resNumP = 0
resNumN = 0
for num in inputList:
    diff = X - num

    if diff > 0:
        diffP = diff
    elif diff < 0:
        diffN = diff

    if abs(diffP) < abs(oldDiffP):
        resNumP = num
    oldDiffP = diffP

    if abs(diffN) < abs(oldDiffN):
        resNumN = num
    oldDiffN = diffN
print(resNumP)
print(resNumN)
"""

""" 
# Сергей Сердюк
k = int(input())
m = abs(k - list_1[0])  # модуль разности
numbers = []  # список для хранения чисел

for i in range(len(list_1)):
    if abs(list_1[i] - k) <= m:
        if abs(list_1[i] - k) < m:
            numbers = []  # очищаем список, если нашли число ближайшее, чем предыдущее
            m = abs(list_1[i] - k)
        numbers.append(list_1[i])
"""
# Таск_20

""" 
# Игорь Москалев
onePoints = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
twoPoints = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
threePoints = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я' ], 3)
fourPoints = dict.fromkeys(['Й', 'Ы'], 4)
fivePoints = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
eightPoints = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
tenPoints = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
mergedDict = onePoints | twoPoints | threePoints | fourPoints | fivePoints | eightPoints | tenPoints 

userText = list(input("Введите одно слово ").upper())
sum = 0
for i in userText:
    sum += mergedDict[i]
print(sum)
"""

""" 
# Павел Кабаков
dict_1 = {'а':1, 'в':1,'е':1,'и':1,'н':1,'о':1,'р':1,'с':1,'т':1,
          'д':2,'к':2,'л':2,'м':2,'п':2,'у':2,
          'б':3,'г':3,'ё':3,'ь':3,'я':3,
          'й':4,'ы':4,
          'ж':5, 'з':5, 'х':5, 'ц':5, 'ч':5,
          'ш':8, 'э':8, 'ю':8,
          'ф':1, 'щ':1, 'ъ':1,}
word = 'ноутбук'
print(f'длинна слова {word} : {len(word)} букв')
summ = 0
for i in range(0, len(word)):
    # print(i)
    # print(word[i])
    # print(dict_1[word[i]])
    # print('---')
    summ = summ + dict_1[word[i]]
print(f'стоимость слова \'{word}\' : {summ} баллов' )
"""

""" 
# Алексей Минченя
eng = "qwertyuiopasdfghjklzxcvbnm"

rus = "йцукенгшщзхъфывапролджэячсмитьбюё"

list_English = {
    1: "AEIOULNSTR",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ",
}
list_Russian = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФШЪ",
}

word = input("Введите слово на русском или английском языке: ")

if word[0].lower() in eng:
    summa = 0
    for letter in word:
        for key, value in list_English.items():
            if letter.upper() in value:
                summa += key
    print(f"стоимость введенного английского слова = {summa}")
else:
    if word[0].lower() in rus:
        summa = 0
        for letter in word:
            for key, value in list_Russian.items():
                if letter.upper() in value:
                    summa += key
    print(f"стоимость введенного русского слова = {summa}")
"""

""" 
# Игорь Москалев
onePoints = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
twoPoints = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
threePoints = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я' ], 3)
fourPoints = dict.fromkeys(['Й', 'Ы'], 4)
fivePoints = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
eightPoints = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
tenPoints = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
mergedDict = onePoints | twoPoints | threePoints | fourPoints | fivePoints | eightPoints | tenPoints 

userText = list(input("Введите одно слово ").upper())
sum = 0
for i in userText:
    sum += mergedDict[i]
print(sum)
"""

# Таск_21

# Таск_23

# Таск_25

""" Сергей Сердюк
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split() """
""" 

# Сергей Сердюк
stroka = input().split()
result = {}
for i in stroka:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1
"""
""" 
# Сергей Сердюк
text = input().split()
set_result = set()
for i in text:
    set_result.add(i.lower())
print(len(set_result))
"""

# Таск_27

""" Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13 """

""" 
# Анастасия Клюсевич
text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".replace(".", " ").split()
set_result = set()
for i in text:
    set_result.add(i.lower())
print(len(set_result))
"""


a=input()
b=input()
m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
        'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
        'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
        'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
        'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
        'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
        'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
        'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
        'Спок-ящерица': 'Руслан'}

""" 
# Алексей Минченя
key = a + "-" + b
print(key)
print(m[key])
"""

# Таск_
""" 
# Сергей Сердюк
На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана.

Формат выходных данных
Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы.
"""


print('- - - - - - - - - - - - - - - - - - ')
print()


