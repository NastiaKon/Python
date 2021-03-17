import os

pathway = None


def default_path():
    global pathway
    pathway = os.path.join(os.getcwd(), os.environ.get("USERNAME"))
    if os.path.isdir(os.environ.get('USERNAME')) is False:
        os.mkdir(pathway)
    else:
        return print('Сдандартная директория уже создана - ', pathway)


default_path()
