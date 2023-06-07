# Реализовать консольное приложение заметки, с
# сохранением, чтением, добавлением, редактированием и удалением заметок.

# Заметка должна содержать:
# идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.

# Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой).

# Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

import os
import uuid
from datetime import datetime


def noteManager():
    print('Вас приветствует кривенькая программа по созданию заметок!' + '\n'
          + 'Почему кривенькая спросите вы?' + '\n'
          + 'Тут все просто, хоть я и выполняю необходимый функционал, качество кода оставляет желать лучшего.' + '\n'
          + 'Просто создатель этого ЧУДА достаточно занят чтобы довести его до ума, так как он учит JS :)' + '\n')
    print('Итак давай приступим к знакомству с моим функционалом' + '\n'
          + 'Ниже ты увидишь все доступные функции. Для работы со мной тебе необходимо вводить номера пунктов ниже.')
    print('А вот и сам список доступных функций, выбирай неспеша: ' + '\n'
          + '1. Создание новой заметки' + '\n'
          + '2. Прочтение конкретной заметки' + '\n'
          + '3. Получение всего списка заметок' + '\n'
          + '4. Редактирование заметки' + '\n'
          + '5. Дополнение заметки' + '\n'
          + '6. Удаление заметки' + '\n'
          + '0. Мы находимся в бесконечном цикле, однако введя 0 ты завершишь работу программы' + '\n')
    your_choice = 8
    while your_choice != 0:
        your_choice = int(
            input('\n' + 'Введите цифру соответствующую нужной функции: '))
        if your_choice == 1:
            creatingNote()
        elif your_choice == 2:
            readNote()
        elif your_choice == 3:
            allNotes()
        elif your_choice == 4:
            editNote()
        elif your_choice == 5:
            addingText()
        elif your_choice == 6:
            removeNote()
        elif your_choice == 0:
            print('Ну ладно.')
        else:
            print('Такую функцию еще не придумали, попробуй снова ;) ')
    else:
        print('Пока-пока!')


def creatingNote():
    title = input('Введите заголовок заметки: ')
    check_title = os.path.exists('./notes/' + title + '.json')
    if (check_title == False):
        text = input('Введите текст заметки: ')
        note_id = str(uuid.uuid4())
        date = str(datetime.now())
        with open(title + '.json', 'w', encoding='utf-8') as file:
            file.write('Заголовок: ' + title + '\n')
            file.write('ID: ' + note_id + '\n')
            file.write('Дата/время создания: ' + date + '\n')
            file.write('\n' + 'Текст: ' + '\n' + text)
        start_position = title + ".json"
        finish_position = './notes/' + start_position
        os.rename(start_position, finish_position)
    else:
        print('Заметка с таким именем уже существует, попробуйте задать другое имя')


def allNotes():
    print('Список всех заметок: ')
    list_files = os.listdir('./notes')
    for i in list_files:
        print(i)


def readNote():
    name = input('Введите имя файла для чтения: ')
    check_name = os.path.exists('./notes/' + name + '.json')
    if (check_name == True):
        with open('./notes/' + name + '.json', 'r', encoding="UTF-8") as file:
            data = file.read()
            print('------------------------------------------------------------------------------'
                  + '\n' + data + '\n' +
                  '------------------------------------------------------------------------------')
    else:
        print('Такого файла не существует')


def editNote():
    name = input('Введите имя файла для редактирования: ')
    check_name = os.path.exists('./notes/' + name + '.json')
    if (check_name == True):
        with open('./notes/' + name + '.json', 'r', encoding="UTF-8") as file:
            data = file.read()
            print('------------------------------------------------------------------------------'
                  + '\n' + data + '\n' +
                  '------------------------------------------------------------------------------')

            old_text = input(
                'Скопируйте и вставьте текст, который хотите изменить: ')
            new_text = input('Введите новый текст: ')
            fin = open('./notes/' + name + '.json', "rt")
            data = fin.read()
            data = data.replace(old_text, new_text)
            fin.close()
            fin = open('./notes/' + name + '.json', "wt")
            fin.write(data)
            fin.close()
            print(
                'Выбранный вами фрагмент текста(если он присутствовал в файле) был заменен')
    else:
        print('Такого файла не существует')


def addingText():
    name = input('Введите имя файла для добавления текста: ')
    check_name = os.path.exists('./notes/' + name + '.json')
    if (check_name == True):
        with open('./notes/' + name + '.json', 'a', encoding="UTF-8") as file:
            file.write(
                '\n' + input('Введите текст, который необходимо добавить: '))
        print('Текст был добавлен в конец заметки.')
    else:
        print('Такого файла не существует')


def removeNote():
    name = input('Введите имя файла для удаления: ')
    check_name = os.path.exists('./notes/' + name + '.json')
    if (check_name == True):
        os.remove('./notes/' + name + '.json')
        print('Файл удален.')
    else:
        print('Такого файла не существует')


noteManager()