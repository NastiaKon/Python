import FileManager

"""1 Создание папки (с указанием имени); 
2 Удаление папки по имени;
3 Перемещение между папками (в пределах рабочей папки) - заход в папку по
имени, выход на уровень вверх;
4 Создание пустых файлов с указанием имени;
5 Запись текста в файл;
6 Просмотр содержимого текстового файла;
7 Удаление файлов по имени;
8 Копирование файлов из одной папки в другую;
9 Перемещение файлов;
10.Переименование файлов."""

while True:
    print("""STOP - остановить программу, NEW - создать папку, RENAME - переименовать файл, DEL - удалить файл,
IN - Переместиться, OUT - Выйти на уровень выше, newf - новый пустой файл, write - запись в файл,
read - просмотр содержимого, delf - удаление файлов, copyf - чтобы скопировать, repl - переместить""")
    comand_1 = str(input('Введи команду: '))
    if comand_1.lower() == 'stop':
        break
    elif comand_1.lower() == 'pwd':
        FileManager.pwd()
    elif comand_1.lower() == 'new':
        FileManager.new_dir()
    elif comand_1.lower() == 'rename':
        FileManager.rename_file()
    elif comand_1.lower() == 'del':
        FileManager.delete_dir()
    elif comand_1.lower() == 'in':
        FileManager.move_in()
    elif comand_1.lower() == 'out':
        FileManager.move_out()
    elif comand_1.lower() == 'newf':
        FileManager.file_create()
    elif comand_1.lower() == 'write':
        FileManager.write()
    elif comand_1.lower() == 'read':
        FileManager.read()
    elif comand_1.lower() == 'delf':
        FileManager.del_f()
    elif comand_1.lower() == 'copyf':
        FileManager.copyf()
    elif comand_1.lower() == 'repl':
        FileManager.replace()
    else:
        print('Я такое не могу!')
