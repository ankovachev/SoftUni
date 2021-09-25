import os


directory = "E:\\py_scripts\\photos\\all\\"


for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        print(os.path.join(root, subdirectory))
    # for file in files:
    #     print(os.path.join(root, file))