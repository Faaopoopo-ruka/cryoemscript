#Author：Alex.Zhang
from sklearn.feature_selection import VarianceThreshold
var=VarianceThreshold(threshold=0.0)
res=var.fit_transform([[10,15,12,16],[15,58,47,69],[47,89,65,12]])
print(res)