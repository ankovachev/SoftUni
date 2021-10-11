import os
from datetime import datetime
from pathlib import Path


# Create a path object
our_files = Path("E:/fox/0/")

# Is the path a file?
print('is_file: ', our_files.is_file())                  # Returns false Дали е файл?

# Is the path a directory?
print('is_dir: ', our_files.is_dir())                   # Returns true Дали е папка?

# What is the parent of the file?
print('parent: ', our_files.parent)                     # Returns /Users/nikpi/Desktop

# What is the base of the filename?
print('stem:   ', our_files.stem)                       # Returns Files Връща пътя

# What are the extensions of the file?
print('suffix: ', our_files.suffix)                     # Returns "" (since it's not a file)

path = Path(args.path)
files = (f for f in path.rglob('*') if f.is_dir())

print(files)