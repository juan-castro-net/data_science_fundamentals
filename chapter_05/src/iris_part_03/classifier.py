# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:04:27 2018

@author: JUANCASTRO
"""


from flask import Flask, request, jsonify
from sklearn.externals import joblib
from flask_cors import CORS
from iswai.iris_mongodb import IrisMongoDB

app = Flask(__name__)
CORS(app)


@app.route('/classify/<float:pl>/<float:pw>/<float:sl>/<float:sw>')
def classify(pl, pw, sl, sw):
    
    # load the saved iris classification model
    model = joblib.load('models/iris_svc.model') 
    
    # make predictions
    data = [pl, pw, sl, sw]    
    predictions = model.predict([data])
    print(type(predictions))

    #return the classification in JSON format
    return jsonify(especies=predictions[0])


@app.route('/classify', methods=['POST'])
def classify_json():
    
    # load the saved iris classification model
    model = joblib.load('models/iris_svc.model') 
    
    #data = request.json
    content = request.get_json() #json
    #print(type(content))
    print(content)
    
    data = []
    for row in content:
        pl = row['pl']
        pw = row['pw']
        sl = row['sl']
        sw = row['sw']
        item = [pl ,pw, sl, sw]
        data.append(item)
    
    #print(data)
    
    #ok data = [[5.1,1.8,5.9,3.0], [4.5,1.5,5.4,3.0], [1.3,0.3,5.0,3.5]]
    # make predictions
    #ok data = [pl, pw, sl, sw]    
       
    predictions = model.predict(data)
    #print(type(predictions))
    print(predictions)
    
    #return the classification in JSON format
    return jsonify(especies=predictions[0])
    #return jsonify(especies=list(predictions))


@app.route('/list', methods=['GET'])
def list():
    
    # load the saved iris classification model
    model = joblib.load('models/iris_svc.model') 
    
    iris_mongodb = IrisMongoDB()
    dataframe = iris_mongodb.getDataframe()
    print(dataframe)
    
    json_data = []
    
    for index, row in dataframe.iterrows():
        pl = row['petal_length']
        pw = row['petal_width']
        sl = row['sepal_length']
        sw = row['sepal_width']
        
        item = [pl ,pw, sl, sw]
        
        category = model.predict([item])[0]
        json_item = {'pl':pl, 'pw':pw, 'sl':sl, 'sw':sw, 'class':category}
        json_data.append(json_item)
    
    print(json_data)
    
    return jsonify(flowers=json_data)
         

if __name__ == '__main__':
   app.run()

