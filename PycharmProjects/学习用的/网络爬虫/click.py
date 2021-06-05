#Author：Alex.Zhang
from selenium import webdriver
import time

from selenium import webdriver
from PIL import Image
#导入时间模块

import time

#创建浏览器对象

driver = webdriver.Chrome()

#打开要操作的网址

driver.get("http://course.ucas.ac.cn/access/content/group/165118/%E5%9B%BD%E7%A7%91%E5%A4%A7%20NMR%E6%8A%80%E6%9C%AF%E5%BA%94%E7%94%A8%EF%BC%88%E4%BA%8C%EF%BC%89.pdf")
driver.save_screenshot('crystall.png')
haha=Image.open('crystall.png')
print(haha.size)
#下面都是获取id属性值为q的节点对象
#
# input = driver.find_element_by_id("q")
# 
# #模拟键盘输入iphone
#
# input.send_keys('iphone')
#
# time.sleep(3)
#
# #清空输入框
#
# input.clear()
#
# #模拟键盘输入iPad
#
# input.send_keys('iPad')
#
# #获取搜索按钮节点
#
# botton = driver.find_element_by_class_name("btn-search")
#
# #触发点击动作
#
# botton.click()