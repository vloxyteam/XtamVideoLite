import glob
import os

list_of_files = glob.glob('/home/xtam/camaras/camara1/*.ts', recursive=True)
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)