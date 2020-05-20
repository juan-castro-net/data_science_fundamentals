from sqlalchemy import create_engine
from sqlalchemy import text
from pandas import DataFrame

class RecPostgres:
    def getConnection(self):
        # create connection
        engine = create_engine('postgresql://recommender01:recommender01@localhost:5432/recommender01')
        return engine

    def getDataframe(self, sql):
        # execute query
        engine = self.getConnection()
        result = engine.execute(sql)
        # convert sqlalchemy.engine.result to pandas dataframe
        dataframe = DataFrame(result.fetchall())
        dataframe.columns = result.keys()
        print(dataframe.head(5))
        return dataframe
    
    def getDataframeRatings(self):
        sql = text('select ratings.user as user_id, item as item_id, rating from ratings')
        df = self.getDataframe(sql)
        return df

rp = RecPostgres()
df = rp.getDataframeRatings()
print(df)


