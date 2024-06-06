#!/usr/bin/python3
"""Pnas api module"""
from flask import Flask, jsonify, request, render_template, url_for
import json
from pymongo import MongoClient
import os
import pyscripts
from pyscripts.pymongoHelper import mongoHelper


app = Flask(__name__, template_folder='export')
app.static_folder = 'static'
jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    comment_start_string='<#',
    comment_end_string='#>',
))
app.jinja_options = jinja_options
storeHelper = mongoHelper()


@app.route("/", strict_slashes=False)
def route_home():
    """display home"""
    return render_template('index.html')


@app.route("/register", methods=['POST'])
def route_handle_register():
    """register a new user"""
    if request.method == 'POST':
        data = request.get_json()
        di = {"msg": storeHelper.addNewUser(data)}
        return jsonify(di)


@app.route("/sms-service", methods=['POST'])
def route_handle_service():
    """add a new sms service"""
    if request.method == 'POST':
        data = request.get_json()
        di = {"msg": storeHelper.addNewSmsService(data)}
        return jsonify(di)


@app.route("/add-sms", methods=['POST'])
def route_handle_addsms():
    """add sms to the stack"""
    msg = ""
    if request.method == 'POST':
        data = request.get_json()

        msg = storeHelper.addSMS(data)
    di = {"msg": msg}
    return jsonify(di)


@app.route("/activate", methods=['POST'])
def route_handle_activate():
    """activate a new user"""
    if request.method == 'POST':
        data = request.get_json()
        di = {"msg": storeHelper.activate(data)}
        return jsonify(di)


@app.route("/getStack", methods=['POST'])
def route_handle_getStack():
    """get sms stack"""
    if request.method == 'POST':
        data = request.get_json()
        return jsonify(storeHelper.getStack(data))
    return "no GET"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
