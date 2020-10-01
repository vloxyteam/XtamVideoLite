#!/bin/bash

#script

find /home/xtam/videos/camara1 -mtime +30 -print &&
find /home/xtam/videos/camara2 -mtime +30 -print &&
find /home/xtam/videos/camara3 -mtime +30 -print &&
find /home/xtam/videos/camara4 -mtime +30 -print
