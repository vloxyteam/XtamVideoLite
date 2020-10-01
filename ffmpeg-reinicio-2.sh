#!/bin/bash
# this script will run until someone kills it
echo PID="$PID"
while true ; do
    startDateTime=$(/bin/date +%Y-%m-%d.%H%M)
    echo "starting ffmpeg at ${startDateTime}"
    ffmpeg -re -i rtsp://192.168.1.88:554/H264?ch=1subtype=1 -f rtsp -muxdelay 0.1 rtsp://18.217.10.249:554/live1.sdp
    # sleep 0.5
done
