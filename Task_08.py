print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- Можно ли от шоколадки размером \'n\'×\'m\' долек отломить k долек,  ---')
print('--- если разрешается сделать один разлом по прямой между дольками ---')
print('--- (то есть разломить шоколадку на два прямоугольника). ---')
print('- - - - - - - - - - - - - - - - - - ')
print()
n = int(input('Введите ширину плитки n: '))
m = int(input('Введите длины плитки m: '))
print(f'Размер плитки {n}x{m}')
k = int(input('Введите количество долек k: '))

if k < m * n and (k % m == 0 or k % n == 0): print('yes')
else: print('no')

print()
