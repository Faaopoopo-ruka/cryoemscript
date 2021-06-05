#Author：Alex.Zhang
from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

# def decision():
#     """
#     决策树对泰坦尼克号进行预测生死
#     :return: None
#     """
#     # 获取数据
#     titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
#
#     # 处理数据，找出特征值和目标值
#     x = titan[['pclass', 'age', 'sex']]
#
#     y = titan['survived']
#
#     print(x)
#     # 缺失值处理
#     x['age'].fillna(x['age'].mean(), inplace=True)
#
#     # 分割数据集到训练集合测试集
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
#
#     # 进行处理（特征工程）特征-》类别-》one_hot编码
#     dict = DictVectorizer(sparse=False)
#
#     x_train = dict.fit_transform(x_train.to_dict(orient="records"))
#
#     print('feature name:',dict.get_feature_names())
#
#     x_test = dict.transform(x_test.to_dict(orient="records"))
#
#     print(x_train)
#
#     dec = DecisionTreeClassifier()
#
#     dec.fit(x_train, y_train)
#     data = np.array([[31, 0, 0.,1,1,0]])
#     y_predict=dec.predict(data.reshape(1, -1))
#     # 预测准确率
#     print("预测的准确率：", dec.score(x_test, y_test))
#
#     print(y_predict)
#     # 导出决策树的结构
#     export_graphviz(dec, out_file="./tree.dot", feature_names=['年龄', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])
# decision()