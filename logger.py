import pandas as pd
import string
import random

df = pd.read_csv("test.csv", sep=";", encoding='UTF-8')

def search_data():                  
    l = len(df.index) - 1
    print("\nПри работе с заметками вы можете: \n Enter - листать и редактировать\n 1 - искать и редактировать по дате или ID")
    var = ' '    
    while var != '' and var != '1':
        var = input('Введите вариант: ')
        print()
        if var == '': flip_note(l)
        elif var == '1': search_note()
        else: print("Неправильный ввод!")

def flip_note(l):
    while l != -1:
        if l != -1:
            print(f"Заметка-{df.iloc [l]['note_ID']} создана: {df.iloc [l]['Time']}")
            print(f"Заголовок: {df.iloc [l]['Heading']}")
            print(f"Содержание: {df.iloc [l]['Text']}")
            print()
        if l == 0: print("Список заметок закончился")    
        var = ' '
        while var != '' and var != '1' and var != '2' and var != '3':
            var = input('Введите Enter - листать, 1 - редактировать, 2 - удалить, 3 - выход: ')
            print()
            if var == '': break
            elif var == '1': 
                edit_note(l)
                l = 0
            elif var == '2': 
                delete_data(l)
                l = 0
            elif var == '3': l = 0
            else: print("Неправильный ввод!")    
        l = l - 1

def read_file():
    print("\nВыведены все имеющиеся заметки:\n")
    l = len(df.index) - 1
    for l in range(len(df.index)):
        print(f"Заметка-{df.iloc [l]['note_ID']} создана: {df.iloc [l]['Time']}")
        print(f"Заголовок: {df.iloc [l]['Heading']}")
        print(f"Содержание: {df.iloc [l]['Text']}")
        print()

def gen_word(length):
    characters = string.ascii_letters + string.digits
    ID_word = ''.join(random.choice(characters) for _ in range(length))
    return ID_word

def new_note():
    t_date = pd.Timestamp.now().strftime('%d-%m-%Y %H:%M')      #получение текущего времени
    text1 = input('Введите текст заголовка: ')
    text2 = input('Введите текст заметки: ')
    df.loc[len(df.index)] = [gen_word(5), t_date, text1, text2]  #добавление новой записи
    df.to_csv("test.csv", sep=";", index=False)                 #сохранение изменений в файле
    print(f"\nНовая заметка с ID: {df.iloc [len(df.index) - 1]['note_ID']} создана: {df.iloc [len(df.index) - 1]['Time']}")
    print(f"Заголовок: {df.iloc [len(df.index) - 1]['Heading']}")
    print(f"Содержание: {df.iloc [len(df.index) - 1]['Text']}")
    print()

def search_note():
    s_text = input('Введите или вставте время создания заметки или её ID: ')
    idx = df.index [(df['Time'] == s_text) | (df['note_ID'] == s_text)].tolist()
    try:
        print(f"Заметка-{df.iloc [idx[0]]['note_ID']} создана: {df.iloc [idx[0]]['Time']}")
        print(f"Заголовок: {df.iloc [idx[0]]['Heading']}")
        print(f"Содержание: {df.iloc [idx[0]]['Text']}")
        print()
    except IndexError:
        print("Введены некоректные данные для поиска!")
        return
    var = ' '    
    while var != '1' and var != '2' and var != '3':
        var = input("Выберите: 1 - редактировать, 2 - удалить, 3 - выйти: ")
        print()
        if var == '1': edit_note(idx[0])
        elif var == '2': delete_data(idx[0])
        elif var == '3': break
        else:  print("Неправильный ввод!")

def edit_note(index_note):
    text1 = input('Введите текст для замены заголовка или Enter, чтобы пропустить: ')
    text2 = input('Введите текст для замены заметки или Enter, чтобы пропустить: ')
    if text1 != '': df.loc[(df.index == index_note), 'Heading'] = text1
    if text2 != '': df.loc[(df.index == index_note), 'Text'] = text2
    df.to_csv("test.csv", sep=";", index=False)
    print("Редактирование завершено:\n")

def delete_data(index_note):
    df.drop(index_note, inplace = True)
    df.to_csv("test.csv", sep=";", index=False)
    print("Заметка удалена!\n")
    