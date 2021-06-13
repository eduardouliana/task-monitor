import json
import time
from core.runner import Runner

def __load_tasks():
    with open('tasks.json') as json_file:
        data = json.load(json_file)

    return data

def main():
    tasks = __load_tasks()
    runner = Runner(tasks)

    while True:
        runner.perform()
        time.sleep(5 * 60)

if __name__ == '__main__':
    main()
