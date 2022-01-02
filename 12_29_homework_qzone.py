import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.maximize_window()
# 窗口最大化
url = "https://qzone.qq.com/"
# 加载需要访问的地址
browser.get(url)

# 开始操作
browser.find_element_by_id("login_div").click()
time.sleep(3)
browser.find_element_by_id("aIcenter").click()
time.sleep(2)
var = browser.find_element_by_id("pageContent").find_element_by_id("QM_Mood_Poster_Container")
var.find_element_by_id("$1_substitutor_content").click()
js = "document.getElementById(\"$1_content_content\").innerHTML=\"以前你都是热烈.\";"
browser.execute_script(js)
var.find_element_by_class_name("btn-post").click()
