print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- требуется написать программу, которая проверяет счастливый ли билета.  ---')
print('- - - - - - - - - - - - - - - - - - ')
print()
num = int(input('Введите номер билета (6 цифр): '))

count = 1
rezR = 0
rezL = 0
st = str(num)

while num > 0:
    if count < 4:
        m = num % 10
        rezR += m
        num //= 10
        count += 1
    else:
        m = num % 10
        rezL += m
        num //= 10
        count += 1

if rezL == rezR:
    print('Билет счастливый !!!')
else:
    print('Билет не счастливый.')


print()
# print(f'Сумма цифр введённого числа = {rez}')
# print()
