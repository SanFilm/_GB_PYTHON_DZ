print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- Три класса нужно оборудовать новыми партами. ---')
print('--- За каждой партой может сидеть два учащихся. ---')
print('--- Известно количество учащихся в каждом классе. ---')
print('--- Выведите наименьшее число парт, которое нужно приобрести для них. ---')
print('- - - - - - - - - - - - - - - - - - ')
print()
a = int(input('Введите количество учащихся 1-го класса: \'a\' = '))
if (a % 2 == 0): ap = a // 2
else: ap = a // 2 + 1
print(f'... {ap} парт')
b = int(input('Введите количество учащихся 2-го класса: \'b\' = '))
if (b % 2 == 0): bp = b // 2
else: bp = b // 2 + 1
print(f'... {bp} парт')
c = int(input('ВВведите количество учащихся 3-го класса: \'c\' = '))
if (c % 2 == 0): cp = c // 2
else: cp = c // 2 + 1
print(f'... {cp} парт')

rez = ap + bp + cp
print()
print(f'... {rez} парт требуется для 3-х классов.')
print()
