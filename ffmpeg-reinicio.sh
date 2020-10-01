#!/bin/bash
# this script will run until someone kills it
echo PID="$PID"
while true ; do
    startDateTime=$(/bin/date +%Y-%m-%d.%H%M)
    echo "starting ffmpeg at ${startDateTime}"
    ffmpeg -re -i rtsp://192.168.1.86:554/rtpvideo1.sdp -y -r 15 -g 600 -an -framerate 15 -vf scale=320:240 -f rtsp rtsp://192.168.1.79:554/live2.sdp
    #ffmpeg -hwaccel_device /dev/dri/renderD128 -re -i rtsp://192.168.1.2:554/rtpvideo1.sdp -y -r 15 -g 600 -an -framerate 15 -vf scale=320:240 -f rtsp rtsp://18.217.10.249:554/live.sdp  
    #ffmpeg -hwaccel_device /dev/dri/renderD128 -re -i rtsp://192.168.1.88:554/H264?ch=1subtype=1 -y -r 15 -g 600 -an -framerate 15 -vf scale=320:240 -f rtsp -muxdelay 0.2 rtsp://18.217.10.249:554/live1.sdp
    sleep 0.5
done
