#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 00:24:41 2018

@author: juancastro
"""

from sqlalchemy import create_engine
from sqlalchemy import text
from pandas import DataFrame

class IrisPostgres:
    
    def getConnection(self):
        # create connection 
        engine = create_engine('postgresql://iris:iris@localhost:5432/iris')
        return engine

    def getDataframe(self):
        # execute query
        sql = text('select sepal_length, sepal_width, petal_length, petal_width, category from iris')     
        engine = self.getConnection()
        result = engine.execute(sql)

        # convert sqlalchemy.engine.result to pandas dataframe
        dataframe = DataFrame(result.fetchall())
        dataframe.columns = result.keys()
        
        print(dataframe.head(5))
        
        return dataframe

    def printData(self):
        # execute query
        sql = text('select * from iris')
        
        engine = self.getConnection()
        result = engine.execute(sql)
        
        for row in result:
            sepal_length = row['sepal_length']
            category = row['category']
            print(sepal_length, category)

