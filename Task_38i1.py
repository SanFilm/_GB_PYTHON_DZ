print()
print('- - - - - - - - - - - - - - - - - - ')
print('--- Дополнить телефонный справочник возможностью изменения и удаления данных. ---')
print('--- Пользователь также может ввести имя или фамилию, ---')
print('--- и Вы должны реализовать функционал для изменения и удаления данных. ---')
print('- - - - - - - - - - - - - - - - - - ')
print()

# -I- -----------------------------------------------------
import pickle
# -F- ------------------------------------------------------


# функция для отображения всего справочника
def show_all():
    for name, phone in address_book.items():
        print(f'{name} - {phone}')

# функция для поиска абонента по фамилии
def find_by_last_name(last_name):
    for name, phone in address_book.items():
        if last_name in name:
            print(f'{name} - {phone}')

# функция для поиска абонента по номеру телефона
def find_by_phone(phone):
    for name, number in address_book.items():
        if phone == number:
            print(f'{name} - {number}')

# функция для добавления нового абонента
def add_entry(name, phone):
    address_book[name] = phone
    print(f'{name} - {phone} has been added')

# функция для удаления абонента из справочника
def delete_entry(name):
    deleted = address_book.pop(name, None)
    if deleted:
        print(f'{name} - {deleted} has been deleted')
    else:
        print(f'{name} was not found in the address book')

# функция для сохранения справочника в бинарном формате
def save_address_book():
    with open('address_book.bin', 'wb') as f:
        pickle.dump(address_book, f)

# функция для загрузки справочника из бинарного формата
def load_address_book():
    global address_book
    with open('address_book.bin', 'rb') as f:
        address_book = pickle.load(f)

# -F- ------------------------------------------------------
# [ ] -------------------------------------------------->->->


# исходные данные
address_book = {
    'Иванов Иван': '111-11-11',
    'Петров Петр': '222-22-22',
    'Сидоров Сидор': '333-33-33'
}

# основной цикл программы
while True:
    print('\nЧто вы хотите сделать?')
    print('1. Отобразить весь справочник')
    print('2. Найти абонента по фамилии')
    print('3. Найти абонента по номеру телефона')
    print('4. Добавить абонента в справочник')
    print('5. Удалить абонента из справочника')
    print('6. Сохранить справочник в бинарном формате')
    print('7. Загрузить справочник из бинарного формата')
    print('8. Закончить работу')

    choice = input('Введите число: ')

    if choice == '1':
        show_all()
    elif choice == '2':
        last_name = input('Введите фамилию: ')
        find_by_last_name(last_name)
    elif choice == '3':
        phone = input('Введите номер телефона: ')
        find_by_phone(phone)
    elif choice == '4':
        name = input('Введите имя и фамилию через пробел: ')
        phone = input('Введите номер телефона: ')
        add_entry(name, phone)
    elif choice == '5':
        name = input('Введите имя и фамилию через пробел: ')
        delete_entry(name)
    elif choice == '6':
        save_address_book()
    elif choice == '7':
        load_address_book()
    elif choice == '8':
        break
    else:
        print('Ошибка ввода')

print('Работа программы завершена.')


# [ ] -------------------------------------------------<-<-<-
print()
print('- - - - - - - - - - - - - - - - - - ')
