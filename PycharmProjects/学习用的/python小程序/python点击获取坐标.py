import time
import pyautogui as pag
import tkinter


def get():
    po.delete( 0 , tkinter.END )
    time.sleep( 1 )  # 几秒后返回位置
    x , y = pag.position()
    po.insert( 0 , str( x ) + ',' + str( y ) )


win = tkinter.Tk()
win.title( "鼠标坐标" )
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry( "%dx%d+%d+%d" % (180 , 80 , (w - 180) / 2 , (h - 80) / 2) )  # 窗口居中、窗口大小180*80
tip = tkinter.Label( win , text="返回点击获取1秒后的光标位置" )
tip.grid( row=0 )
po = tkinter.Entry( win )
po.grid( row=1 )
do = tkinter.Button( win , text="获取" , command=get )  # 点击获取位置
do.grid( row=2 )

win.mainloop()