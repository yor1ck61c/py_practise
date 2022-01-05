import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.maximize_window()
# 窗口最大化
url = "https://www.che168.com/china/benchi/"
# 加载需要访问的地址
browser.get(url)
# 获取当前页面的信息
# 开始操作

car_infos = browser.find_element_by_id("goodStartSolrQuotePriceCore0").find_elements_by_css_selector("ul li")
car_info = car_infos[0]
print(browser.find_element_by_css_selector("a div+div h4").text)
# 奔驰GLC 2017款 GLC 260 4MATIC 豪华型
print(browser.find_element_by_css_selector("a div+div p").text)
# 5万公里／2017-05／上海／2年钻石商家
print(browser.find_element_by_css_selector("a div+div div span").text)
# 26.98万

# count = 0
# range(x), 取前x页数据。总数据量为 105 + 56(x-1) 个
# for i in range(6):
#     car_infos = browser.find_element_by_id("goodStartSolrQuotePriceCore0").find_elements_by_css_selector("ul li")
#     count += len(car_infos)
#     browser.find_element_by_id("listpagination").find_element_by_link_text("下一页").click()
# print(count)
# 翻页
# browser.find_element_by_id("listpagination").find_element_by_link_text("下一页").click()
# time.sleep(3)
# browser.quit()

