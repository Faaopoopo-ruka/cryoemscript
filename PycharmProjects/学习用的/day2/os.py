
#Author：Alex.Zhang
'''
import os
print(os.system('dir'))
'''
'''
import os
cmd_dir=os.system('dir')
print(cmd_dir)
'''
'''
import os
cmd_dir=os.system('dir')#只执行结果
print(cmd_dir)
'''

import os
cmd_dir=os.popen('dir').read()
print(cmd_dir)
os.mkdir('调试创建的文件')