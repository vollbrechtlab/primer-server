#!/usr/bin/env python

"""
REST API for primerDAFT.
It uses a separate thread for each task request.
"""

__author__ = "Takao Shibamoto"
__copyright__ = "Copyright 2017, Vollbrecht Lab"
__date__ = "3/27/2018"


import json, os
from flask import Flask, jsonify, abort, request, make_response, url_for, send_file, send_from_directory, Response
from flask_cors import CORS

from task_thread import *
from utilities import *

from version import __version__
basicRoute = '/v'+__version__+'/'


# Flask app
app = Flask(__name__, static_url_path = "")
CORS(app)

# create cache folder if it doesnt exist yet
if not os.path.exists("cache"):
    os.makedirs("cache")

""" Error Handling """

@app.errorhandler(400)
def not_found(error):
    """ handle 400 error
    """
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    """ handle 404 error
    """
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


""" Route handling """
    
@app.route(basicRoute, methods = ['GET'])
def welcome():
    """ Say welcome
    """
    return "Welcome to our primer server REST API"


@app.route(basicRoute+'result/<string:taskId>', methods = ['GET'])
def getResult(taskId):
    """ Handle GET request to get a specific result
        Calculate the primer and return it
    Args:
        param1: Task ID
    Returns:
        JSON of the task result
    """

    result = None
    try: # result file exists in cache already
        # load result data and return it
        result = loadResultFile(taskId)
    except Exception as e: # result file does not exist
        abort(404)

    try: # load the result from file
        if result['status'] == 'in process':
            return jsonify( { 'status':'in process'} ), 201

        elif result['status'] == 'ok':
            # load task
            task = loadTaskFile(taskId)

            # make task result
            taskResult = {}
            taskResult['status'] = 'ok'
            taskResult['result'] = result['result']
            taskResult['task'] = task

            return jsonify(taskResult), 201

        elif result['status'] == 'error':
            return jsonify( { 'status':'error', 'error_statement': result['error_statement']} ), 201

    except Exception as e:
        return jsonify( { 'status':'error', 'error_statement': 'result is broken'} ), 400
    

@app.route(basicRoute, methods = ['POST'])
def addTask():
    """ Handle POST request to add a new primer3 task
    Returns:
        URL of the task result url
    """

    task = request.json

    # input_data key doesn't exist
    if not 'primer3_data' in task:
        return jsonify( { 'status':'error', 'error_statement': 'task doesn\'t have primer3_data field'} ), 400

    # SEQUENCE_TEMPLATE key doesn't exist
    if not 'SEQUENCE_TEMPLATE' in task['primer3_data']:
        return jsonify( { 'status':'error', 'error_statement': 'task[\"input_data\"] JSON doesn\'t have SEQUENCE_TEMPLATE field'} ), 400

    taskId = idGenerator()
    task['taskId'] = taskId
    startTask(task)

    # return the id of the result
    return jsonify( { 'status': 'ok', 'taskId': taskId} ), 201

if __name__ == '__main__':
    app.run(debug = True, port=8001)
    #app.run(host='0.0.0.0', port='8001')
