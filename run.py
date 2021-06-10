from jobs.redmine import Redmine
from datetime import datetime, time
import time as timer

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
    __30Minutes = 60 * 30    

    while True:
        if _itsTimeToWork():
            Redmine().sendN3TasksNotification()
        timer.sleep(__30Minutes)

if __name__ == '__main__':
    main()