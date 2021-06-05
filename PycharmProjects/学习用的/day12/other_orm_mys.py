#Author：Alex.Zhang
#创建表的另一种方式
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer , String , ForeignKey , UniqueConstraint , Index
from sqlalchemy.orm import sessionmaker , relationship
from sqlalchemy import create_engine
