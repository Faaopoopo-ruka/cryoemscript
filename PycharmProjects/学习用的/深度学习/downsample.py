#Author：Alex.Zhang
import pandas as pd
from sklearn.decomposition import PCA
import csv
crime=pd.read_csv('crime.csv',engine='python')

cross=pd.crosstab(crime['OFFENSE_CODE_GROUP'],crime['STREET'])
pca=PCA(n_components=0.9)
data=pca.fit_transform(cross)
print(data)
