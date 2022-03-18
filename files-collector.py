# Считаем, файлы для обработки лежат в папке Sorted в том же каталоге что и обработчик
import os

def files_collector():
    os.chdir('Sorted')
    file_list = os.listdir()
    file_len_dict = {}
    file_content_dic = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            file_len_dict[file] = len(f.readlines())
            f.seek(0, 0)
            file_content_dic[file] = f.read()
            f.flush()
    sorted_files = sorted(file_len_dict, key=file_len_dict.get, reverse=True)
    with open('result.txt', 'a', encoding='utf-8') as w:
        for file in sorted_files:
            w.write(file + '\n')
            w.write(str(file_len_dict[file]) + '\n')
            w.write(file_content_dic[file] + '\n')

files_collector()
