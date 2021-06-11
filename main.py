#from jobs.redmine import Redmine

from datetime import datetime, time
import time as timer
import json

def __loadTasksConfig():
    with open('tasks.json') as json_file:
        data = json.load(json_file)

    return data        

def _itsTimeToWork():
    startTime = time(8,0)
    endTime = time(18,0)
    currentTime = datetime.now().time()

    if currentTime < startTime:
        return False
    if currentTime > endTime:
        return False
    return True

def main():
    tasksConfig = __loadTasksConfig()

    for config in tasksConfig:
        task = 

    while True:
        for task in tasks:
            
        if _itsTimeToWork():
            Redmine().sendN3TasksNotification()
        timer.sleep(__30Minutes)

if __name__ == '__main__':
    main()