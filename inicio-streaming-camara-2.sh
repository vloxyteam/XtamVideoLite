#!/bin/bash

#script de ejemplo

ffmpeg -hwaccel_device /dev/dri/renderD128 -re -i rtsp://192.168.1.88:554/H264?ch=1subtype=1 -y -r 15 -g 600 -an -framerate 15 -vf scale=320:240 -f rtsp -muxdelay 0.2 rtsp://18.217.10.249:554/live1.sdp
