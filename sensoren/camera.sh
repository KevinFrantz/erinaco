#!/bin/bash
# @param string $1 Client-Ip
# @author kf
# @since 2017-10-22
#
# Streamt ein Video auf Vaio
#/opt/vc/bin/raspivid --hflip --vflip -t 0 -o - | nc 192.168.178.30 5001
#
# Auf Vaio muss 
# nc -l -p 5001 | mplayer -fps 31 -cache 1024 -
# ausgefuehert werden

clientname="$1.fritz.box"
# main
if [ "$#" -gt "0" ]
	then 
		sudo /opt/vc/bin/raspivid  -w 640 -h 480 --hflip --vflip -t 0 -o - | nc $1 5001
else
		head -n 11 camera.sh
		echo "Es wurden nicht alle benoetigten Parameter uebergeben"
fi
