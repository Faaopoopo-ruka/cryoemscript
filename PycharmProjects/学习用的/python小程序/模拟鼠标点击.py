#Author：Alex.Zhang
from pykeyboard import *
from pymouse import *
import time

m = PyMouse()
k = PyKeyboard()
a=397
m.click(1069, 397)
# m.click(883, 402)
# m.click(883, 458)
# m.click(886, 493)
# m.click(885, 548)
# m.click(882, 582)

for i in range(15):
     m.click(1069, a+i*30 )


# time.sleep(3)
# print(m.position())
# time.sleep(3)
# print(m.position())
# time.sleep(3)
# print(m.position())
# time.sleep(3)
# print(m.position())
# time.sleep(3)
# print(m.position())
# x_dim, y_dim = m.screen_size()
# print(x_dim,y_dim)