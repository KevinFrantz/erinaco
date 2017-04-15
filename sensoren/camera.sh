#!/bin/bash
#Streamt ein Video auf Vaio
/opt/vc/bin/raspivid -t 0 -o - | nc 192.168.178.30 5001
#Auf Vaio muss 
# nc -l -p 5001 | mplayer -fps 31 -cache 1024 -
# ausgefuehert werden
