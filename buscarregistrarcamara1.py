#!/usr/bin/env python2 #or python2.6 or python3 or even python3.1
#!/usr/bin/env python
from datetime import datetime
import os
import mariadb
import glob
import listarcam1 as lst1
import sys, codecs
import locale
import revisartamano1 as tam
import daystart as ds
import timestart as tis
import duracion as dur
import datefinish as df
import timefinish as tf
import datetimestart as dts

print (sys.getdefaultencoding())

#1 nombre del archivo - filename
filename = lst1.latest_file

#2 obtener el tamaño del archivo - size
tam = tam.os.path.getsize(filename) 
#print('El tamaño es de: ', tam, 'bytes')

#3 comienzo del tiempo - datestart
ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

df = df.get_duration(filename)

#4 comienzo de tiempo - timestart
dts = dts.x

#5 Tiempo de inicio del video
tiv = tis

#6 listados de los archivos ts
dn = lst1.latest_file

#7 Dia Final


#8 duracion del archivo
dt = dur.get_duration(filename)

#7 tiempo final del archivo
tf = tf.x

#8 Dia de modificación
di = os.stat('/').st_mtime

#9 Tiempo de modificacion
hi = os.stat('/').st_ctime




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
    cur.execute("INSERT INTO recordings (id, filename, type, size, datestart, timestart, datefinish, timefinish, idCamara, datetimestart, datetimefinish) VALUES ( NULL, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?)", (filename, '.ts', tam, ts, ts, dts, df, 1, ts, tf))

except mariadb.Error as e:
    print(f"Error: {e}")
  
# Finalizar 
conn.commit()
print (f"Último Insertado desde camara 1: {cur.lastrowid}")
conn.close()



