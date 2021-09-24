import os, shutil

source_dir = 'C:\\Users\\User\\Desktop\\file2'
destination_dir = 'C:\\Users\\User\\Desktop\\file1'

files = os.listdir(source_dir)

for f in files:
    shutil.move(os.path.join(source_dir, f), destination_dir)