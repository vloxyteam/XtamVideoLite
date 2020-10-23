import glob
import os

list_of_files3 = glob.glob('/home/xtam/camaras/camara3/*.ts', recursive=True)
latest_file3 = max(list_of_files3, key=os.path.getctime)
print(latest_file3)

