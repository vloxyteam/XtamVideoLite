# /bin/sh
# ./record.sh -i 192.168.0.47:554 -v 11 -r 1280x720
# Some sane defaults for the environment.
DATE=`date +%Y-%m-%d`
TIME=`date +%H-%M-%S`
CAMERA_USER='root'
CAMERA_PASS='pass'
CAMERA_IP='rtsp://192.168.1.85:554'
CAMERA_NAME='cam1'

# Destination for recordings. Directors
DEST_DIR=$CAMERA

# Duration of segments in seconds.
SEGMENT_DURATION='5'

# Group of Pictures size.
GOP_SIZE='12'

# Output resolution.
RECORDING_RESOLUTION='720x576'

# Path to to the camera stream.
VIDEO_PATH='/stream1'

# Help printer.

function help {
    echo "Usage: record.sh [OPTION]"
    echo "Launch FFMPEG against the specified RTSP stream and tee the result"
    echo "to disk | udp."
    echo " "
    echo "-u            camera username"
    echo "-p            camera password"
    echo "-i            camera IP address or hostname"
    echo "-n            aamera name, used when creating an output"
    echo "              directory"
    echo "-s            duration of recorded segments in seconds."
    echo "-d            top level destination directory. Recordings"
    echo "              will be placed in a <name> subdirectory."
    echo "-v            path to the camera RTSP stream. Typically"
    echo "              /video, /stream, /h264 or similar."
    echo "-r            recording resolution in the form '640x480'"
    echo "-g            GOP size used when recording."
    echo "-h            display this help and exit."
    echo "-o            seconary output desination"
}

# Simple command line argument handling.
while getopts ':u:p:i:n:s:d:v:r:g:h' flag
    
do
    case $flag in
        u) CAMERA_USER=$OPTARG;;
        p) CAMERA_PASS=$OPTARG;;
        i) CAMERA_IP=$OPTARG;;
        n) CAMERA_NAME=$OPTARG;;
        s) SEGMENT_DURATION=$OPTARG;;
        d) DEST_DIR=$OPTARG;;
        v) VIDEO_PATH=$OPTARG;;
        r) RECORDING_RESOLUTION=$OPTARG;;
        g) GOP_SIZE=$OPTARG;;
        h) help; exit 0;;
        \?) help; exit 2;;
    esac
done

DEST='./'$CAMERA_NAME

# make the directories
rm -rf $DEST
mkdir -p $DEST
mkdir -p $DEST/segments

[ -d $DEST ] || mkdir -p $DEST

echo ${DEST}/${DATE}_${TIME}_%05d.webm
ffmpeg -re -i rtsp://$CAMERA_USER:$CAMERA_PASS@$CAMERA_IP/$VIDEO_PATH \
  -profile:v baseline \
  -level 5.0 \
  -an \
  -f hls \
  -reset_timestamps 1 \
  -movflags faststart \
  -s $RECORDING_RESOLUTION \
  -start_number 0 -hls_time 10 -hls_list_size 0 \
  -use_localtime 1 -hls_segment_filename "$%Y%m%d-%s.ts" \
  "${DEST}/index.m3u8"
