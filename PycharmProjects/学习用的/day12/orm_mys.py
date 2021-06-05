#Author：Alex.Zhang
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String , ForeignKey , UniqueConstraint , Index,ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker , relationship
from sqlalchemy import create_engine,

engine = create_engine( "mysql+pymysql://root:root@localhost/oldboydb" ,encoding='utf-8')

Base = declarative_base()


# 创建单表
class User(Base):
    __tablename__ = 'hehe' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    def __repr__(self):
        return ('name:%s,password:%s'%(self.name,self.password))
Base.metadata.create_all(engine)
Session_class = sessionmaker( bind=engine )  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例
#user_obj = User( name="zhn" , password="alex3714" )  # 生成你要创建的数据对象
#user_obj2 = User( name="ybb" , password="alex3714" )  # 生成你要创建的数据对象
# print( user_obj.name , user_obj.id )  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
#Session.add( user_obj,user_obj2 )  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print( user_obj.name , user_obj.id )  # 此时也依然还没创建
data=Session.query(User).filter_by(id=1).filter_by(name='alex')#查询的方法#多条件查询
data.name='jiji'#修改的方法，就是通过面向对象的方法
#hehe=Session.query(User).filter(User.id<1).all()#查询的方法,filter的方法


Session.commit()  # 现此才统一提交，创建数据