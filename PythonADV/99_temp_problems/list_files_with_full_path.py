import os


# def list_files(start_path):
#     for root, dirs, files in os.walk(start_path):
#         level = root.replace(start_path, '').count(os.sep)
#         indent = ' ' * 4 * level
#         #  print('{}{}/'.format(indent, os.path.basename(root)))
#         print(f'{start_path}{os.path.basename(root)}')
#         sub_indent = ' ' * 4 * (level + 1)
#         for f in files:
#             #  print('{}{}'.format(sub_indent, f))
#             print(f'{start_path}{os.path.basename(root)}')
#
#
# base_dir = f'E:/fox/'
# list_files(base_dir)


root_dir = 'E:\\fox\\'
for file in os.listdir(root_dir):
    d = os.path.join(root_dir, file)
    if os.path.isdir(d):
        print(d)


def list_dirs(root_dir):
    for it in os.scandir(root_dir):
        if it.is_dir():
            print(it.path)
            list_dirs(it)
            if it.path == "0":
                os.rename(os.path.join(root_dir, it.dir), os.path.join(root_dir, 'Bravo'))

list_dirs(root_dir)
