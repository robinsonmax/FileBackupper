#Run this script every 15 minutes

#Define folders to copy below
files=['world','world_nether','world_the_end']

import shutil,datetime,os

date = datetime.datetime.now().strftime("%Y%m%d %H-%M-%S")

folderBackup = 'BACKUP'
folderRecent = '1. Last 16'
folderHour = '2. Hourly'
folderDay = '3. Daily'

def copy(fileFrom,fileTo):
    print('Copying {fileFrom} to {fileTo}'.format(fileFrom=fileFrom,fileTo=fileTo))
    shutil.copytree(fileFrom,fileTo)

def move(fileFrom,fileTo):
    print('Moving {fileFrom} to {fileTo}'.format(fileFrom=fileFrom,fileTo=fileTo))
    shutil.move(fileFrom,fileTo)

def delete(file):
    print('Deleting {file}'.format(file=file))
    shutil.rmtree(file)

def getFiles(folder):
    return next(os.walk(folder))[1]

def getDayAndHour(fileName):
    try:
        return fileName.split('-')[0]
    except:
        return ''

def getDay(fileName):
    try:
        return fileName.split(' ')[0]
    except:
        return ''

#Copies all world files into 15 minute folder
for i in range(len(files)):
    file=files[i]
    copy(file, folderBackup+'/'+folderRecent+'/'+date+'/'+file)


filesRegularFolder = getFiles(folderBackup+'/'+folderRecent)
filesInHourlyFolder = getFiles(folderBackup+'/'+folderHour)
filesInDailyFolder = getFiles(folderBackup+'/'+folderDay)

#While there are more than 10 files in the minute folder, iterate through the extra files (the oldest first)
while(len(filesRegularFolder) > 16):
    #If no files are in the hourly folder, just move the extra file there
    if(len(filesInHourlyFolder) == 0):
        move(folderBackup+'/'+folderRecent+'/'+filesRegularFolder[0],folderBackup+'/'+folderHour+'/'+filesRegularFolder[0])
    else:
        #If there is already a file from the same day & hour in the hourly folder, just delete the extra file
        if(getDayAndHour(filesRegularFolder[0]) == getDayAndHour(filesInHourlyFolder[-1])):
            delete(folderBackup+'/'+folderRecent+'/'+filesRegularFolder[0])
        else:
            move(folderBackup+'/'+folderRecent+'/'+filesRegularFolder[0],folderBackup+'/'+folderHour+'/'+filesRegularFolder[0])
    filesRegularFolder.pop(0)

#While there are more than 24 files in the hourly folder, iterate through the extra files (oldest first)
while(len(filesInHourlyFolder) > 24):
    #If the most recent file in the daily folder has the same day, delete the existing daily backup one first
    if(getDay(filesInHourlyFolder[0]) == getDay(filesInDailyFolder[-1])):
        delete(folderBackup+'/'+folderDay+'/'+filesInDailyFolder[-1])
    move(folderBackup+'/'+folderHour+'/'+filesInHourlyFolder[0],folderBackup+'/'+folderDay+'/'+filesInHourlyFolder[0])
    filesInHourlyFolder.pop(0)
