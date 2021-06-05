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


def naviebayes():
    """
    朴素贝叶斯进行文本分类
    :return: None
    """
    news = fetch_20newsgroups(subset='all')
    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计['a','b','c','d']
    x_train = tf.fit_transform(x_train)
    x_predict='''There are moments in life when you miss someone so much that you just want to pick them from your dreams and hug them for real! Dream what you want to dream;go where you want to go;be what you want to be,because you have only one life and one chance to do all the things you want to do.

May you have enough happiness to make you sweet,enough trials to make you strong,enough sorrow to keep you human,enough hope to make you happy? Always put yourself in others’shoes.If you feel that it hurts you,it probably hurts the other person, too.

The happiest of people don’t necessarily have the best of everything;they just make the most of everything that comes along their way.Happiness lies for those who cry,those who hurt, those who have searched,and those who have tried,for only they can appreciate the importance of people

who have touched their lives.Love begins with a smile,grows with a kiss and ends with a tear.The brightest future will always be based on a forgotten past, you can’t go on well in lifeuntil you let go of your past failures and heartaches.'''

    x_predict=tf.transform([x_predict])
    # print(tf.get_feature_names())
    # print(x_train, y_train)
    x_test = tf.transform(x_test)
    # 进行朴素贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)
    mlt.fit(x_train, y_train)

    # y_predict = mlt.predict(x_test)
    # print("预测的文章类别为：", y_predict)
    # print(y_test)

    # 得出准确率
    # print("准确率为：", mlt.score(x_test, y_test))

    # print("每个类别的精确率和召回率：", classification_report(y_test, y_predict, target_names=news.target_names))
    print(mlt.predict(x_predict))
    return None
naviebayes()

