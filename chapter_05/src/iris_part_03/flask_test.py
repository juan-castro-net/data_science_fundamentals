# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:05:33 2018

@author: JUANCASTRO
"""

from flask import Flask, jsonify
from iswai.iris_mongodb import IrisMongoDB
from iswai.iris_postgres import IrisPostgres
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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



"""
https://machinelearningmastery.com/
machine-learning-in-python-step-by-step/
"""
    
@app.route('/demo')
def build_demo():
    # Check the versions of libraries

    # Python version
    import sys
    print('Python: {}'.format(sys.version))
    # scipy
    import scipy
    print('scipy: {}'.format(scipy.__version__))
    # numpy
    import numpy
    print('numpy: {}'.format(numpy.__version__))
    # matplotlib
    import matplotlib
    print('matplotlib: {}'.format(matplotlib.__version__))
    # pandas
    import pandas
    print('pandas: {}'.format(pandas.__version__))
    # scikit-learn
    import sklearn
    print('sklearn: {}'.format(sklearn.__version__))
    
    
    # Load libraries
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    
    # Load dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pandas.read_csv(url, names=names)



    # shape
    print(dataset.shape)

    # head
    print(dataset.head(20))

    # descriptions
    print(dataset.describe())

    # class distribution
    print(dataset.groupby('class').size())

    # box and whisker plots
    dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    plt.show()


    # histograms
    dataset.hist()
    plt.show()


    # scatter plot matrix
    scatter_matrix(dataset)
    plt.show()

    
    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:4]
    Y = array[:,4]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
    
    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'


    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
    	kfold = model_selection.KFold(n_splits=10, random_state=seed)
    	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    	results.append(cv_results)
    	names.append(name)
    	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    	print(msg)
        
    
    # Compare Algorithms
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()

    
    # Make predictions on validation dataset
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))
    

if __name__ == '__main__':
   app.run()