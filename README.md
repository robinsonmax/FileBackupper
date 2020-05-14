# FileBackupper
Python script used for backing up my Minecraft server

Set this script to run every 15 minutes or so to automatically save folders specified on line 4 of the python file.

The script will copy each of the given local directories into a folder named with the time of the script executing

Saves are split into 3 folders:

* A folder containing the most recent 16 backups
* A folder for every hour of last 24 hour period
* A folder with a backup from every day
