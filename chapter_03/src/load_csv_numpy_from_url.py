# Load CSV from URL using NumPy
from numpy import loadtxt
from urllib.request import urlopen
url = 'https://raw.githubusercontent.com/juancasi/data_science_fundamentals/'
url += 'master/chapter_03/datasets/pima-indians-diabetes.csv'
raw_data = urlopen(url)
dataset = loadtxt(raw_data, delimiter=",")
print(dataset.shape)