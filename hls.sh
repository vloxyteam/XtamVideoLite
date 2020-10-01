#/bin/bash

ffmpeg -i rtsp://192.168.1.86:554/rtpvideo1.sdp -fflags flush_packets -max_delay 2 -flags -global_header -hls_time 10 -hls_list_size 3 -vcodec copy -y /home/xtam/camaras/camara1/video-camara-1.m3u8
