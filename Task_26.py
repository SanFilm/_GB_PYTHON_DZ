print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- Напишите программу, которая на вход принимает два числа A и B, ---')
print('--- и возводит число А в целую степень B с помощью рекурсии.  ---')
print('- - - - - - - - - - - - - - - - - - ')
print()
# [ ] -------------------------------------------------->->->

# -F- ------------------------------------------------------
def ExpoRecursIf(A, B):
    if B == 0:
        return 1
    return A * ExpoRecursIf(A, B - 1)

def ExpoRecursWhile(A, B):
    while B != 0:
        return A * ExpoRecursWhile(A, B - 1)
    return 1
# -F- ------------------------------------------------------


A = int(input('Введите число: '))
B = int(input('Введите степень числа: '))
print()
print(f'Результат равен {ExpoRecursIf(A, B)}')
print(f'{A} в степени {B} -> {ExpoRecursWhile(A, B)}')
print(f'{A}^{B} = {ExpoRecursWhile(A, B)}')
print(f'{A} ** {B} = {ExpoRecursWhile(A, B)}')
# print(A, '**', B, '=', A**B)

# [ ] -------------------------------------------------<-<-<-
print()
print('- - - - - - - - - - - - - - - - - - ')
