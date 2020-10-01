#!/bin/bash

#script de ejemplo

ffmpeg -re -i rtsp://192.168.1.86:554/rtpvideo1.sdp -an -framerate 15 -vf scale=320:240 -f rtsp rtsp://192.168.1.79:8554/live/test
