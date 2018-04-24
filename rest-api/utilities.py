#!/usr/bin/env python

"""
small utility functions
"""

__author__ = "Takao Shibamoto"
__copyright__ = "Copyright 2017, Vollbrecht Lab"
__date__ = "9/30/2017"

import json, random, string


def loadTaskFile(taskId):
    return json.load(open('cache/'+taskId+'_task.json', 'r'))


def loadResultFile(taskId):
    return json.load(open('cache/'+taskId+'_result.json', 'r'))

def loadResultCSV(taskId):
	return open('cache/'+taskId+'_result.csv', 'r')


def idGenerator(size=16, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

