#Author：Alex.Zhang
import pandas as pd
import csv
import matplotlib.pyplot as plt
def handler():
    data1={'series':['C7','C8','C9','C10','C11','C12','D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12'],
          '260_280':[1.7,1.36,1.19,1.25,1.29,1.20,1.30,1.06,0.99,0.84,0.79,0.67,0.71,0.73,0.82,0.92,1.10]}
    data={}
    dic_to_vsc=pd.DataFrame(data).to_csv('xiaomao.csv')
    show_once=pd.DataFrame(data)
    print(show_once)
def plot_it():
    data = pd.read_csv( '12.9.2019.csv' )
    y = data['mAU']
    x=data['ml']
    plt.plot( x,y )
    plt.xticks( rotation=90 )
    plt.xlabel( 'Flow through(ml)' )
    plt.ylabel( 'OD280(mAU)' )
    plt.title( 'Molecular sieve peak diagram' )
    plt.savefig( '小猫给的第三组数据.jpg' )
    plt.show()
def plot_mutiple():
    data = pd.read_csv( '12.9.2019.csv' )
    plt.title( 'Result Analysis' )
    plt.plot( x_axix , train_acys , color='green' , label='training accuracy' )
    plt.plot( sub_axix , test_acys , color='red' , label='testing accuracy' )
    plt.plot( x_axix , train_pn_dis , color='skyblue' , label='PN distance' )
    plt.plot( x_axix , thresholds , color='blue' , label='threshold' )
    plt.legend()  # 显示图例

    plt.xlabel( 'iteration times' )
    plt.ylabel( 'rate' )
    plt.show()
def read():
    data = pd.read_csv( '22.csv' )
    print(data['ml1'].decode('utf8'))


plot_it()