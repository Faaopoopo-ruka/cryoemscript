#Author：Alex.Zhang
import time,multiprocessing,threading

def threading_run():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print('hehe%s'%name)
    t=threading.Thread(target=threading_run())
    t.start()
if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process( target=run,args=('bob',) )
        p.start()
        print( '第%s次' % i )

