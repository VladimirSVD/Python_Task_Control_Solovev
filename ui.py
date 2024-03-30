from logger import search_data, new_note, read_file

def interface():
    print("Программа для создания и редактирования заметок.\n\nВыберите вариант: \n 1 - Вывод всех заметок из файла \n 2 - Поиск, редактирование или удаление \n 3 - Создание новой заметки \n 4 - Выход из программы")
    command = ''
    while command != '1' and command != '2' and command != '3':
        command = input('Введите номер: ')
        if command == '1': read_file()
        elif command == '2': search_data()
        elif command == '3': new_note()
        elif command == '4': return print("Вы вышли из программы.")
        else: print("Неправильный ввод!")