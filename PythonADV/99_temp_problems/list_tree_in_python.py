import os
from os import path
from os import chdir
from os.path import realpath
from os.path import dirname

# open('sample-a.txt', 'w')
# confirm = input('Are you sure ....?')
# if confirm == 'y':
# if path.exists('sample-a.txt'):
#     os.remove('sample-a.txt')
#
# [print(x) for x in os.listdir('.')]
# print('-----')
# [print(x) for x in os.listdir('lab')]

base_dir = 'E:\\fox\\'
ss = [base_dir]
number = 1
files = []
while ss:
    current_dir = ss.pop()
    number += 1
    print('--------------- > ', current_dir)
    if path.isfile(current_dir):
        print(current_dir)
        files.append(current_dir)
        continue

    for file_path in os.listdir(current_dir):
        absolute_path = path.join(current_dir, file_path)
        print('                                 absolute_path -- >', absolute_path)
        if not path.isfile(current_dir):
            new_file = 'NNN' + str(number) + '.txt'
            new_file_name = path.join(current_dir, new_file)
            print(f'                          Current_dir: {current_dir} and file is: {file_path}')
            print('                                 absolute_path -- >', absolute_path)
            print(f'                             new_file_name will be: {new_file_name}')

            with open(new_file_name, 'a') as file:
                file.write('Това е текст на Български!')
        ss.append(absolute_path)

#
# for file_name in os.listdir(base_dir):
#     full_path = path.join(
#         os.getcwd(),
#         file_name
#     )
#     print(full_path)
