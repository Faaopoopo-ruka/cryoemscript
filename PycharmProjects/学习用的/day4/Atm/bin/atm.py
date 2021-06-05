#Author：Alex.Zhang
import os
import sys
print(__file__)
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
print(sys.path)
sys.path.append(base_dir)
print(__file__)
# from core import main
# main.func(6)
import core
core.func(6)