import os
import fnmatch
import os 
from pprint import pprint 

    
# Walking a directory tree and printing the names of the directories and files
for dirpath, dirnames, files in os.walk('/home/xtam/camaras/'):
    print(f'Directorio Encontrado: {dirpath}')
    for file_name in files:
        print(file_name)
        
files = []

for dirname, dirnames, filenames in os.walk('/home/xtam/camaras/'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        files.append(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        files.append(os.path.join(dirname, filename))


pprint(files)
