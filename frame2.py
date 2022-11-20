"""
frame 操作: 从 frame 切换到 frame
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get(r'C:\Users\22982\Desktop\page\注册实例.html')

# 案例：打开‘注册实例.html’页面，完成以下操作
# 1). 填写主页面的注册信息
driver.find_element_by_id('user').send_keys('admin')
driver.find_element_by_id('password').send_keys('123456')

# 2). 填写注册页面A中的注册信息
# 说明: 如果目标元素存在于 frame 中, 就需要先执行切换 frame 操作, 再定位元素
# 切换 frame: 传入的是能够代表 frame 元素唯一性的特征值
driver.switch_to.frame('idframe1')
driver.find_element_by_id('userA').send_keys('admin1')
driver.find_element_by_id('passwordA').send_keys('123456')

# 切换回默认页面: 如果连续切换多个 frame, 必须先回到默认页面, 才能实现切换下一个 frame
driver.switch_to.default_content()

# 切换 frame
driver.switch_to.frame('myframe2')

# 3). 填写注册页面B中的注册信息
driver.find_element_by_id('userB').send_keys('admin2')
driver.find_element_by_id('passwordB').send_keys('123456')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()
