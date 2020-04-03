# Load CSV using Pandas
from pandas import read_csv
filename = '../datasets/pima-indians-diabetes.csv'
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(filename, names=names)
print(data.shape)