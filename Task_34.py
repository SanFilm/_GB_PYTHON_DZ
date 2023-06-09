print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. ---')
print('--- Ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. ---')
print('--- Фраза может состоять из одного слова. Если во фразе несколько слов, то они разделяются дефисами. ---')
print('--- Фразы отделяются друг от друга пробелами. Стихотворение вводится с клавиатуры. ---')
print('--- В ответе напишите “Парам пам-пам”, если с ритмом все в порядке ---')
print('--- и “Пам парам”, если с ритмом все не в порядке. ---')
print()
print('- 1. - - - - - - - - - - - - - - - - ')
print()
# -I- -----------------------------------------------------

# -F- -------------------------------------------------->->->
def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])

# -F- -------------------------------------------------<-<-<-
# [ ] -------------------------------------------------->->->

str_1 = 'Пара-ра-рам рам-пам-папам па-ра-па-дам'
print('Исходный ритм:\n', str_1)
print()
if rhythm(str_1):
    print('!!!-  Парам пам-пам  -!!!')
else:
    print('Пам парам')
print()

print('- 2. - - - - - - - - - - - - - - - - ')

# Дмитрий Пешков
input = "пара-ра-рам рам-пам-папам па-ра-па-дам"
letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
a = list(map(lambda x: len(list(filter(lambda y: y in letters, x))), input.split()))
print()
if max(a) == min(a):
    print("Парам пам-пам")
else:
    print("Пам парам")

# [ ] -------------------------------------------------<-<-<-
print()
print('- - - - - - - - - - - - - - - - - - ')
