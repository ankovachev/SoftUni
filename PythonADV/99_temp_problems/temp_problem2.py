import os.path
current_path = "E:\\py_scripts\\photos\\all\\"
file_name = "pic_1.jpg"
if os.path.isfile(current_path + file_name):
    print("File exist")
else:
    print("File not exist")
print(current_path)
print(file_name)
print(current_path + file_name)
