#Author：Alex.Zhang
from sklearn.model_selection import train_test_split, GridSearchCV
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
def knn():
    data=pd.read_csv('aa.csv',engine='python')
    data=data.query('REPORTING_AREA>100')
    data=data.drop('INCIDENT_NUMBER',axis=1)
    data=data.drop('OFFENSE_DESCRIPTION',axis=1)
    data=data.drop('OFFENSE_CODE_GROUP',axis=1)
    #取出来目标值
    y=data['REPORTING_AREA']#'目标值'
    x=data.drop('REPORTING_AREA',axis=1)
    #进行数据分割
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)
    print(x_train)
    knn=KNeighborsClassifier(n_neighbors=1)
    knn.fit(x_train,y_train)
    y_predict=knn.predict(x_test)
    print(y_predict,y_test)
    print(knn.score(x_test,y_test))
if __name__ == "__main__":
    knn()
