print()
print('- - - - - - - - - - - - - - - - - - ')

print()
# 51
""" 
Павел Кабаков
def same_by(characteristic, objects):
    for i in objects:
        if (characteristic(objects[0])) != (characteristic(i)):
            return False
    return True

values = [0, 2, 10, 6]
# values = []
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
 """
""" 10:10
Сергей Сердюк
def same_by(func, collection):
    return len(list(filter(func, collection))) == 0

10:10
 """
print()
print('- - - - - - - - - - - - - - - - - - ')
print()

# 34
""" Дмитрий Пешков
input = "пара-ра-рам рам-пам-папам па-ра-па-дам"
letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
a = list(map(lambda x: len(list(filter(lambda y: y in letters, x))), input.split()))
if max(a) == min(a):
    print("Парам пам-пам")
else:
    print("Пам парам")
 """
""" 10:17
Сергей Сердюк
for i in phrases:
		countVowels.append(len([x for x in i if x.lower() in vowels]))
	
	if countVowels.count(countVowels[0]) == len(countVowels):
		print('Парам пам-пам')
	else:
		print('Пам парам')
 """
10:17

print()
print('- - - - - - - - - - - - - - - - - - ')
print()

# 36
""" Дмитрий Пешков
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        print(*list(map(operation, [i] * num_columns, range(1, num_columns + 1))))

print_operation_table(lambda x, y: x * y)
 """
10:34

print()
print('- - - - - - - - - - - - - - - - - - ')
print()
""" 
Сергей Сердюк
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')


    while (choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

work_with_phonebook()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


 """
""" 
x.rjust     # добавление символов.
(20)
 """



print()
print('- - - - - - - - - - - - - - - - - - ')


