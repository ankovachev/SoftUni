import os


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    print(f'Directory is: {directory}')
    if not os.path.exists(directory):
        print(f"Folder {directory} created with success!")
        os.makedirs(directory)
    else:
        print(f"Folder {directory} exist!  Nothing to do....")


def create_dirs(folder_path):
    for i in range(18):
        for j in range(5):
            for number_of_folder in range(4):
                base_dir = f'{folder_path}/{i}/{j}/{number_of_folder}/'
                print(f"Basedir = {base_dir}")
                ensure_dir(base_dir)


create_dirs('E:/fox/')
