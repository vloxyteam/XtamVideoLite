#!/usr/bin/env python2 #or python2.6 or python3 or even python3.1
#!/usr/bin/env python
from datetime import datetime
import os
import mariadb
import glob
import listarcam1 as lst1
import sys, codecs
import locale
import revisartamano1 as rt1

print (sys.getdefaultencoding())

ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
filename = lst1.latest_file
dn = lst1.latest_file

# get the size of file
tam = rt1.os.path.getsize(filename) 
#print('El tamaño es de: ', tam, 'bytes')


conn = mariadb.connect(
  user="xtam",
  password="Xtam2020",
  host="localhost",
  database="xtam"
)

cur = conn.cursor()

def result():
    resultado = [y for x in os.walk("") for y in glob(os.path.join (x[0], '*.ts'))]
 #   print ("Resultado : %s" % resultado)

nom = dir

try:
    cur.execute("INSERT INTO recordings (id, filename, type, size, datestart, timestart, datefinish, timefinish, idCamara, datetimestart, datetimefinish) VALUES ( NULL, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?)", (filename, '.ts', tam, ts, ts, ts, ts, 1, ts, ts))

except mariadb.Error as e:
    print(f"Error: {e}")
  
# Finalizar 
conn.commit()
print (f"Último Insertado desde camara 1: {cur.lastrowid}")
conn.close()


