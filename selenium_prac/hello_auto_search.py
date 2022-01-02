import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.maximize_window()
# 窗口最大化
url = "https://www.baidu.com"
browser.get(url)
# 使用get方法访问网站

element_kw = browser.find_element_by_id("kw")
# kw是输入框的id, 这句话相当于把输入框拿过来
element_kw.send_keys("666")
# send_key方法可以模拟给输入框传递参数
element_btn = browser.find_element_by_id("su")
element_btn.click()
# 有了输入就可以模拟点击提交按钮，获取到btn按钮之后调用click方法可以点击
result = browser.find_element_by_id('head')

print(result.text)
time.sleep(20)
browser.quit()
