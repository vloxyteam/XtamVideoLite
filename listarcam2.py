import glob
import os

list_of_files2 = glob.glob('/home/xtam/camaras/camara2/*.ts', recursive=True)
latest_file2 = max(list_of_files2, key=os.path.getctime)
print(latest_file2)
