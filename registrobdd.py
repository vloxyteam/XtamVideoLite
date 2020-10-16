from datetime import datetime
import os
import mariadb
import glob
import listador as lst

ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
filename = lst.file_name
dn = lst.file_name

# get the size of file
tam = os.path.getsize('/home/xtam/camaras/') 
print('El tamaño es de: ', tam, 'bytes')

conn = mariadb.connect(
  user="xtam",
  password="Xtam2020",
  host="localhost",
  database="xtam"
)

cur = conn.cursor()

def result():
    resultado = [y for x in os.walk("/home/xtam/camaras/") for y in glob(os.path.join (x[0], '*.ts'))]
 #   print ("Resultado : %s" % resultado)

nom = dir

try:
    cur.execute("INSERT INTO recordings (id, filename, type, size, datestart, timestart, datefinish, timefinish, idCamara, datetimestart, datetimefinish) VALUES ( NULL, ? , ?, ?, ?, ?, ?, ?, ?, ?, ?)", (filename, 'ts', tam, ts, ts, ts, ts, 0, ts, ts))

except mariadb.Error as e:
    print(f"Error: {e}")
  
# Finalizar 
conn.commit()
print (f"Último Insertado: {cur.lastrowid}")
conn.close()



