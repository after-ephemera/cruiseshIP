#!/bin/sh
# Set a cron job to run cruiseshIP periodically.
echo 'Starting cruiseshIP setup...'

hours=$1
echo "Creating cron job to run every day at ${hours} hours..."
pathToScript=$(realpath ./cruiseshIP.py)
logDirectory=$(dirname $pathToScript)

#write out current crontab
crontab -l > mycronjob
#echo new cron into cron file
echo "* * * ${hours} 0 python3 ${pathToScript} > ${logDirectory}/output.txt" >> mycronjob
#install new cron file
crontab mycronjob
rm mycronjob
