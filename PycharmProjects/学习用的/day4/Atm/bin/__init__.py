#Author：Alex.Zhang
import os
import sys
print(__file__)
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# from core import main
# main.func(6)
import core
core.func(6)