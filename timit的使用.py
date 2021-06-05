import time
import threading
def dance():
    for i in range(5):
        print("---dancing---")
        time.sleep(1)
        print(time.ctime())
def sing():
    for i in range(5):
        print("---singing---")
        time.sleep(1)
        print(time.ctime())
def main():
    t1 = threading.Thread(target = dance)
    t2 = threading.Thread(target = sing)
    t1.start()
    t2.start()
if __name__ == '__main__':
    main()
