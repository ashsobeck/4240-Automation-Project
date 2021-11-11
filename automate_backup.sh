#!/bin/bash

echo "Starting backup of home dir now!"
date_of_backup=`date +"%d-%b-%Y"`
unix_time_now=`date +%s`
filename="$date_of_backup-$unix_time_now.tar.gz"
echo $filename
bucketname=""
# tar -czvf /home /tmp/backup/$filename
echo "Finished backup, running cloud backup..."
