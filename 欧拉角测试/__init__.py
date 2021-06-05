
import math
import sys
import re
from numpy import *


phi = 170 / 180 * math.pi
theta = 10 / 180 * math.pi
psi = 60 / 180 * math.pi


r11 = math.cos(psi) * math.cos(theta) * math.cos(phi) - math.sin(psi) * math.sin(phi)
r12 = math.cos(psi) * math.cos(theta) * math.sin(phi) + math.sin(psi) * math.cos(phi)
r13 = -math.cos(psi) * math.sin(theta)

r21 = -math.sin(psi) * math.cos(theta) * math.cos(phi) - math.cos(psi) * math.sin(phi)
r22 = -math.sin(psi) * math.cos(theta) * math.sin(phi) + math.cos(psi) * math.cos(phi)
r23 = math.sin(psi) * math.sin(theta)

r31 = math.sin(theta) * math.cos(phi)
r32 = math.sin(theta) * math.sin(phi)
r33 = math.cos(theta)

a=[r11,r12,r13]
b=[r21,r22,r23]
c=[r31,r32,r33]
juzhen=matrix([a,b,c])
print(juzhen)

a3=juzhen*juzhen
print(a3)


new_x = r11 + r12  + r13
new_y = r21  + r22 + r23
new_z = r31 + r32 + r33
