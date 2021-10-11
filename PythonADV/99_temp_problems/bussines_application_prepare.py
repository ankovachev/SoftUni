import os  # the os module need to be imported

# print(os.listdir('e:/fox'))  # here the location is ‘/usr’  # Print all subdirs
# print(os.getcwd()) #print the current location
os.chdir('e:/fox')

# print current working directory
print(f'Current folder is: {os.getcwd()}')

folder_to_create = "data2"
if not os.path.exists(folder_to_create):
    os.mkdir(folder_to_create)


#rename directory

folder_to_rename = "data2"
destination_folder = 'data_ruse-3'
a = 5


if os.path.exists(folder_to_rename) and (not os.path.exists(destination_folder)):
    os.rename(folder_to_rename, destination_folder)
    print('Raname ---- >')
else:
    print('Nothing to do')

print(os.listdir(os.getcwd()))