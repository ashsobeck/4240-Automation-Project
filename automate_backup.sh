#!/bin/bash

# if [[  ! -d '/backups/' ]]; then
#   mkdir /backups/
# fi
test ! -d ~/backups && mkdir ~/backups
echo "Starting backup of home dir now!"
date_of_backup=`date +"%d-%b-%Y"`
unix_time_now=`date +%s`
filename="$date_of_backup-$unix_time_now.tar.gz"
echo $filename
bucketname="4240-backup-bucket-for-vm-presentation-f21"
tar -czvf  ~/backups/$filename --exclude="*.tar.gz" --exclude="*.env" ~/*
echo "Finished backup, running cloud backup..."
python3 ~/4240-Automation-Project/backup.py -f ~/backups/$filename -b $bucketname 
