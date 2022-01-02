import time
from selenium import webdriver
browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.maximize_window()
# 窗口最大化
url = "https://www.airbnb.cn"
browser.get(url)
# 使用get方法访问网站
# 点击同意并继续
browser.find_element_by_class_name("_ybm5hv2").click()
# 获取当前页面句柄
before_handle = browser.current_window_handle
# print(before_handle)
# 获取输入框，输入长沙，获取搜索按钮，点击搜索
browser.find_element_by_id("Koan-via-HeroController__input").send_keys("长沙")
browser.find_element_by_class_name("_1je6u3q").click()
time.sleep(2)
# 找到日期按钮，打开选日期菜单
browser.find_element_by_id("menuItemButton-date_picker").click()
# 找到特定日期按钮，选一个日期
browser.find_element_by_class_name("_1wh4xpp1").click()
# 找到确认按钮，确定日期
browser.find_element_by_class_name("_dae0b4e").click()
time.sleep(1)
# 找到选人数按钮，打开选人数菜单
browser.find_element_by_id("menuItemButton-guest_picker").click()
time.sleep(1)
# 成年人+1
browser.find_element_by_class_name("_1a72ixey").click()
# js = "var elem_append_adult_btn=document.getElementsByClassName('_hvw2ivt'); elem_append_adult_btn[0].click()"
# browser.execute_script(js)
browser.find_element_by_class_name("_dae0b4e").click()
time.sleep(2)
# 点击第一个链接
browser.find_element_by_class_name("_okj6x").click()

# 此时打开了新的页面，需要获取新页面句柄然后选中新页面再进行预定
time.sleep(5)

all_handles = browser.window_handles
for i in all_handles:
    if i != before_handle:
        browser.switch_to.window(i)
# 点击预约按钮
browser.find_element_by_class_name("_ptje086").click()
