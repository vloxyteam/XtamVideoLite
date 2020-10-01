#/bin/sh/


ffmpeg -hwaccel_device /dev/dri/renderD128  -i rtsp://192.168.1.86:554/rtpvideo1.sdp -an -codec:v libx264 -preset superfast -crf 36  -f ssegment -strftime 1 -segment_time 524 -reset_timestamps 1 /home/xtam/camaras/c1/xtam-%Y-%m-%d_%H-%M-%S.mp4 & ffmpeg -hwaccel_device /dev/dri/renderD128  -i rtsp://192.168.1.85:554/H264?ch=1subtype=1 -an -codec:v libx264 -preset superfast -crf 36  -f ssegment -strftime 1 -segment_time 524 -reset_timestamps 1 /home/xtam/camaras/c2/xtam-%Y-%m-%d_%H-%M-%S.mp4
exit 
