#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 00:24:55 2018

@author: juancastro
"""

from flask import Flask, jsonify
from iswai.iris_mongodb import IrisMongoDB
from iswai.iris_postgres import IrisPostgres

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = {'id':123,'name':'Flask test'}  
    return jsonify(message)

@app.route('/mongodb')
def mongodb():
    iris_mongodb = IrisMongoDB()
    dataframe = iris_mongodb.getDataframe()
    data_json = dataframe.to_json(orient='records')
    return jsonify(data_json)

@app.route('/postgres')
def postgres():
    iris_postgres = IrisPostgres()
    dataframe = iris_postgres.getDataframe()
    data_json = dataframe.to_json(orient='records')
    return jsonify(data_json)

if __name__ == '__main__':
   app.run()
