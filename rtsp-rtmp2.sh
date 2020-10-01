#!/bin/bash

# script

ffmpeg -rtsp_transport tcp -i rtsp://192.168.1.86:554/rtpvideo1.sdp -framerate 30 -video_size 1280x720 -vcodec libx264 -preset veryfast -maxrate 1984k -bufsize 3968k -vf "format=yuv420p" -g 60 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://192.168.1.79:1935/live/test2 
