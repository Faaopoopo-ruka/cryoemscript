
#Author：Alex.Zhang
import sys,os
x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(x)
sys.path.append(x)
from day4 import Atm
from Atm import bin
from bin import atm
