import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.maximize_window()
# 窗口最大化
url = "https://www.che168.com/china/benchi/#pvareaid=108402#listfilterstart"
# 加载需要访问的地址
browser.get(url)

# 开始操作
browser.find_element_by_class_name("")