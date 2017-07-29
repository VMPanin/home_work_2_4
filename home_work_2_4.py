import os

def get_current_dir():
    current_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Migrations\\')
    return current_dir

def get_sql_files():
    files = os.listdir(get_current_dir())
    sql_files =[]
    for file in files:
        if file.endswith('.sql') == True:
            sql_files.append(file)
    return sql_files

def find_file():
    files = get_sql_files()
    while True:
        find_str = input('Введите строку из файла:')
        for file in files:
            with open(os.path.join(get_current_dir(), file)) as f:
                read_file = f.read()
                if (find_str in read_file) == False:
                    files.remove(file)
        print('\n'.join(files),'\nВсего:',len(files))

find_file()
