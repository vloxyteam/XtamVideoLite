#/bin/bash

# en la ruta de salida, se debe cambiar por la que se desea guardar

ffmpeg -i rtsp://192.168.1.85:554/H264?ch=1subtype=1 -fflags flush_packets -max_delay 2 -flags -global_header -hls_time 60 -hls_list_size 3 -vcodec copy -y /home/xtam/camaras/camara1/camara-1.m3u8
