import os
import shutil
import Sett

pathway = Sett.pathway
os.chdir(pathway)
ban = os.path.join(pathway, os.pardir)


def pwd():
    path = os.getcwd()
    print("Текущая директория: ", path)


def new_dir():
    dir_1 = str(input('Введи имя новой папки: '))
    if not os.path.isdir(dir_1):
        os.mkdir(dir_1)
        print('Файл ', dir_1, ' создан!')
    else:
        print('--------------Папка с таким названием уже существует! --------------')


def rename_file():  # И папки
    name_1 = str(input('Введи имя файла: '))
    name_2 = str(input('Введи новое имя файла: '))
    if os.path.isdir(name_1):
        os.rename(name_1, name_2)
        print('Папка ', name_1, ' переименована на ', name_2)
    elif os.path.isfile(name_1):
        os.rename(name_1, name_2)
        print('Файл ', name_1, ' переименован на ', name_2)
    else:
        print('--------------Не могу переименовать --------------')


def delete_dir():
    del_1 = str(input('Введи имя папки для удаления: '))
    if not os.path.isdir(del_1):
        return print('--------------Папки с таким названием нет--------------')
    else:
        shutil.rmtree(del_1)
        print('Папка ', del_1, ' удалена!')


def move_in():
    mv_1 = str(input('Папка для перемещения: '))
    dir = os.path.isdir(os.path.join(pathway, mv_1))
    if dir:
        os.chdir(mv_1)
    else:
        return print('--------------Папки с таким названием нет--------------')


def move_out():
    path = os.getcwd()
    parent = os.path.join(path, os.pardir)
    if os.path.abspath(parent) == os.path.abspath(ban):
        print('--------------Доступ ограничен--------------')
    else:
        os.chdir(os.path.abspath(parent))


def file_create():
    # создать новый текстовый файл
    text_file = str(input('Введи имя нового файла: '))
    if not os.path.isfile(text_file):
        open(text_file, "w")
    else:
        print('--------------Такой файл уже есть --------------')


def write():
    # запить текста в этот файл
    text_file = str(input('Введи имя файла: '))
    if not os.path.isfile(text_file):
        print('--------------Такого файла нет--------------')
    else:
        text_file = open(text_file, "w")
        text = str(input('Что желаете записать?: '))
        text_file.write(text)


def read():
    text_file = str(input('Введи имя файла: '))
    if not os.path.isfile(text_file):
        print('--------------Такого файла нет--------------')
    else:
        text_file = open(text_file, "r")
        for line in text_file:
            print(line)


def del_f():
    text_file = str(input('Введи имя файла: '))
    if not os.path.isfile(text_file):
        print('--------------Такого файла нет--------------')
    else:
        os.remove(text_file)


def replace():
    name = str(input('Введите имя того, что надо переместить: '))
    dir = str(input('Введите имя папки: '))
    dir1 = os.path.isdir(os.path.join(pathway, dir))
    file1 = os.path.isfile(os.path.join(pathway, name))
    if dir1:
        os.replace(os.path.join(pathway, name), os.path.join(pathway, dir, 'repl1'))
        return print('Папка ', os.path.join(pathway, name), 'перемещена в ', os.path.join(pathway, dir, 'repl1'))
    elif file1:
        os.replace(os.path.join(pathway, name), os.path.join(pathway, dir))
        return print('Файл ', os.path.join(pathway, name), 'перемещен в ', os.path.join(pathway, dir, 'repl1'))
    else:
        return print('--------------Что-то указано не правильно--------------')


def copyf():
    name = str(input('Введите имя файла: '))
    dir = str(input('Введите имя папки: '))
    dir1 = os.path.isdir(os.path.join(pathway, dir))
    file1 = os.path.isfile(os.path.join(pathway, name))
    if dir1 and file1:
        shutil.copyfile(os.path.join(pathway, name), os.path.join(pathway, dir, 'new'))
        return print('Файл ', os.path.join(pathway, name), 'копирован в ', os.path.join(pathway, dir, 'new'))
    elif file1 is False:
        return print('--------------Файл не найден--------------')
    else:
        return print('--------------Директория не найдена--------------')
