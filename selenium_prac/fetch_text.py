import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.maximize_window()
# 窗口最大化
url = "https://www.baidu.com"
# 加载需要访问的地址
browser.get(url)

# 开始操作
lists = browser.find_element_by_class_name("s-bottom-layer-content").find_elements_by_class_name("lh")
for i in lists:
    print(i.text)
