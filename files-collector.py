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





# print(files_collector())








# def files_collector(path1=None, path2=None, path3=None):
#     if path1 or path2 or path3 is None:
#         path1 = '1.txt'
#         path2 = '2.txt'
#         path3 = '3.txt'
#         os.chdir('sorted')
#         outout_file = "rewrite_file.txt"
#         file1_path = os.path.join(os.getcwd(), path1)
#         file2_path = os.path.join(os.getcwd(), path2)
#         file3_path = os.path.join(os.getcwd(), path3)
#         with open(file1_path, 'r', encoding='utf-8') as f1:
#             file1 = f1.readlines()
#         with open(file2_path, 'r', encoding='utf-8') as f2:
#             file2 = f2.readlines()
#         with open(file3_path, 'r', encoding='utf-8') as f3:
#             file3 = f3.readlines()
#         with open(outout_file, 'w', encoding='utf-8') as f_total:

#             if len(file1) < len(file2) and len(file1) < len(file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#                 f_total.write('\n')
#             elif len(file2) < len(file1) and len(file2) < len(file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#                 f_total.write('\n')
#             elif len(file3) < len(file1) and len(file3) < len(file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#                 f_total.write('\n')
#             if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
#                     file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#                 f_total.write('\n')
#             elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
#                     file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#                 f_total.write('\n')
#             elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
#                     file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#                 f_total.write('\n')
#             if len(file1) > len(file2) and len(file1) > len(file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#             elif len(file2) > len(file1) and len(file2) > len(file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#             elif len(file3) > len(file1) and len(file3) > len(file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#     else:
#         print('Давай лучше без параметров')
#     return
