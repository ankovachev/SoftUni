# import
import os

# define current working directory
cwd = 'E:\\py_scripts\\photos'
count = 1
for dir_path, dir_names, file_names in os.walk(cwd):
    for f in file_names:
        if f.endswith('.jpg') or f.endswith('.JPG'):
            dest_dir = os.path.join(cwd, 'all')
            # create new directory if does not exist
            if not os.path.isdir(dest_dir):
                os.mkdir(dest_dir)
            while True:
                new = 'jpg_pic_' + str(count) + '.jpg'
                full_file_name = dest_dir + "\\" + new
                print(full_file_name)
                if not os.path.isfile(full_file_name):
                    os.rename(os.path.join(dir_path, f), os.path.join(dest_dir, new))
                    break
                count += 1
        count = 1
