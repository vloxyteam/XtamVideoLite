import glob
import os

list_of_files4 = glob.glob('/home/xtam/camaras/camara4/*.ts', recursive=True)
latest_file4 = max(list_of_files4, key=os.path.getctime)
print(latest_file4)


