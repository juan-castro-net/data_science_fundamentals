# Load CSV using Pandas from URL
from pandas import read_csv
url = 'https://raw.githubusercontent.com/juancasi/data_science_fundamentals/'
url += 'master/chapter_03/datasets/pima-indians-diabetes.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(url, names=names)
print(data.shape)