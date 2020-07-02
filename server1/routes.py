import time
import random
import celery
from flask import Flask, jsonify, request, url_for, current_app as app
from helpers import json_result


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/text/<int:id>', methods=['GET'])
def get(id: int):
    return jsonify(json_result(True, ""))


@app.route('/text', methods=['GET'])
def get_all():
    return jsonify(json_result(True, ""))


@app.route('/text/save/<name>', methods=['POST'])
def save(name: str):
    return jsonify(json_result(True, ""))

@celery.task
def example_task():
    return "status"

@celery.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(1)
    return {'current': 100,
            'total': 100,
            'status': 'Task completed!',
            'result': 42}


@app.route('/task/longtask', methods=['GET'])
def longtask():
    task = example_task.()
    return jsonify({}), 202, {'Location': url_for('taskstatus', task_id=task.id)}


@app.route('/task/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
