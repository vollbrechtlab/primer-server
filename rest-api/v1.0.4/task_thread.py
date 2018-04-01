#!/usr/bin/env python

"""
A thread to find primers from task
"""

__author__ = "Takao Shibamoto"
__copyright__ = "Copyright 2017, Vollbrecht Lab"
__date__ = "3/27/2018"


import threading, json, string, random, logging, os
import fakePrimerDAFT

# create log folder if it doesnt exist yet
if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logs/task.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def worker(task):
    """thread worker function"""

    saveTask(task)
    print('new task added ' + task['taskId'])
    logger.info('new task added ' + task['taskId'])
    
    result = {}
    result['status'] = 'in process'
    result['taskId'] = task['taskId']

    saveResult(result)

    result = fakePrimerDAFT.run(task)
    result['taskId'] = task['taskId']
    print('result made: ' + result['taskId'])
    logger.info('result made: ' + result['taskId'])

    saveResult(result)


def saveResult(result):
    resultPath = 'cache/'+result['taskId']+'_result.json'
    # save the result to a file
    with open(resultPath, 'w') as resultFile:
        json.dump(result, resultFile, sort_keys = True, indent = 4, ensure_ascii = False)


def saveTask(task):
    """ Save a task to a file
    Args:
        newTask: new task name
        taskId: new task ID
    """

    taskPath = 'cache/'+task['taskId']+'_task.json'

    # save input data as json file
    with open(taskPath, 'w') as taskFile:
        json.dump(task, taskFile)


def startTask(task):
	threads = []
	t = threading.Thread(target=worker, args=(task,))
	threads.append(t)
	t.start()
