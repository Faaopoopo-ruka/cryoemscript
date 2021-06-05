#Author：Alex.Zhang
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler,MinMaxScaler
stand=StandardScaler(with_mean=1)
data=stand.fit_transform([[10,15,12,16],[15,58,47,69],[47,89,65,12]])
print(data)