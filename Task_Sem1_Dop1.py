print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- Напишите программу, которая найдёт произведение пар чисел списка.  ---')
print('--- Парой считаем первый и последний элемент, второй и предпоследний и т.д. ---')
print('- - - - - - - - - - - - - - - - - - ')
print()

# Нашёл на просторах интернета.
def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)


lst = [2, 3, 4, 5, 6]
mult_lst(lst)
lst = [1, 2, 3, 4, 5, 6, 7]
mult_lst(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

print()
