from flask import Flask, jsonify, request, current_app as app
from helpers import json_result



@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/text/<int:id>', methods=['GET'])
def get(id: int):
    return jsonify(json_result(True, ""))


@app.route('/text', methods=['GET'])
def get_all():
    return jsonify(json_result(True,""))


@app.route('/text/save/<name>', methods=['POST'])
def save(name: str):
    return jsonify(json_result(True, ""))



