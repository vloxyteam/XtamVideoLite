#!/bin/bash
# Script de instalación de librerias y software.
# Esta etapa debe estar el xtam conectado a una red con internet.
echo "Bienvenido al instalador de Xtam!"
echo "Atienda a las preguntas que se haran mientras se instala el software"

sudo apt update
# Install Nginx
# mas información https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md

sudo apt install nginx
sudo /etc/init.d/nginx start

# PHP
sudo apt install php-fpm

# Activar Nginx
cd /etc/nginx
sudo nano sites-enabled/default

# Recargar el Nginx
sudo /etc/init.d/nginx reload
cd /var/www/html/
sudo mv index.nginx-debian.html index.php
sudo nano index.php

echo "Saliendo del instalador Xtam!"

# FTP
# mas información https://www.raspberrypi-spy.co.uk/2018/05/creating-ftp-server-with-raspberry-pi/

# Instalar vsftpd

sudo apt-get update
sudo apt-get install vsftpd

# Actualizar el archivo de configuracion

sudo nano /etc/vsftpd.conf

# Revisar el archivo y configurar el mismo con estos parametros:

#anonymous_enable=NO
#local_enable=YES
#write_enable=YES
#local_umask=022
#chroot_local_user=YES
 
# agregar estas lineas al final del archivo:

user_sub_token=$USER
local_root=/home/$USER/ftp

#Crear Directorio FTP para el usuario pi:

mkdir /home/pi/ftp
mkdir /home/pi/ftp/videos

# cambiar los permisos del directorio FTP:

chmod a-w /home/pi/ftp

# Mas informacion en: https://www.raspberrypi-spy.co.uk/2018/05/creating-ftp-server-with-raspberry-pi/

# Reiniciar FTP
sudo service vsftpd restart

# Logs de Sesiones

cat /var/log/vsftpd.log

# Nginx RTMP

sudo apt-get update
sudo apt-get install libnginx-mod-rtmp

# Si hay un error consultar: https://www.itsfullofstars.de/2020/01/nginx-with-rtmp-on-raspberry-pi-as-a-streaming-server-for-obs/

# Activar RTMP
cd /etc/nginx/
sudo nano rtmp.conf
 
# Agregar estas lineas

#rtmp {
#  server {
#    listen 1935;
#    chunk_size 4096;
#    application live {
#      live on;
#      record off;
#    }
#  }
#}

cd /etc/nginx/nginx.conf

# Agregar:
include /etc/nginx/rtmp.conf;

# Iniciar Nginx con RTMP

sudo systemctl stop nginx.service
sudo systemctl start nginx.service
sudo systemctl status nginx.service

netstat -an | grep 1935



exit
