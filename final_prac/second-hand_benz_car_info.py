import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/Administrator/Desktop/py_practise/driver/chromedriver.exe')
browser.maximize_window()
# 窗口最大化
url = "https://www.che168.com/china/benchi/"
# 加载需要访问的地址
browser.get(url)
# 开始操作
# 定义变量
car_class = ""
car_launch_time = 2020
car_drive_mode = ""
is_AMG = 0
had_refit = 0
is_import = 0
mileage = 0
release_year = 2000
release_month = 6
release_area = "长沙"
seller_time = 2022
seller_type = ""
car_price = 0

# 定义方法
def set_first_string(str1, car_class, car_launch_time, car_drive_mode, is_AMG, had_refit, is_import):
    if "AMG" in str1:
        is_AMG = 1
        str1.replace("AMG", "")
    if "改" in str1:
        had_refit = 1
        str1.replace("改款", "")
    if "进" in str1:
        is_import = 1
        str1.replace("(进口)", "")
    if "4MATIC" in str1:
        car_drive_mode = "4MATIC"
        str1.replace("4MATIC", "")
    infos = str1.split(" ")
    car_class = infos[0].replace("奔驰", "").replace("级", "")
    car_launch_time = infos[1].replace("款", "")

def set_second_string(str2, mileage, release_year, release_month, release_area, seller_time, seller_type):
    infos = str2.split('／')

    mileage = float(infos[0].replace("万公里", "")) * 10000

    date_info = infos[1].split('-')
    release_year = int(date_info[0])
    release_month = int(date_info[1])

    release_area = infos[2]

    seller_info = infos[3].replace("年", "").replace("商家", "")
    seller_time = seller_info[0]
    seller_type = seller_info[1:3]

def set_car_price(car_price):
    return int(float(car_price.replace("万", "")) * 10000)


# range(x), 取前x页数据。总数据量为 105 + 56(x-1) 个
for i in range(6):
    time.sleep(3)
    car_infos = browser.find_element_by_id("goodStartSolrQuotePriceCore0").find_elements_by_css_selector("ul li")
    for car_info in car_infos:
        str1 = car_info.find_element_by_css_selector("a div+div h4").text
        if "奔驰" not in str1:
            continue
        else:
            if "AMG" in str1:
                is_AMG = 1
                str1.replace("AMG", "")
            if "改" in str1:
                had_refit = 1
                str1.replace("改款", "")
            if "进" in str1:
                is_import = 1
                str1.replace("(进口)", "")
            if "4MATIC" in str1:
                car_drive_mode = "4MATIC"
                str1.replace("4MATIC", "")
            infos = str1.split(" ")
            car_class = infos[0].replace("奔驰", "").replace("级", "")
            car_launch_time = infos[1].replace("款", "")
        str2 = browser.find_element_by_css_selector("a div+div p").text
        infos = str2.split('／')

        mileage = float(infos[0].replace("万公里", "")) * 10000

        date_info = infos[1].split('-')
        release_year = int(date_info[0])
        release_month = int(date_info[1])

        release_area = infos[2]

        seller_info = infos[3].replace("年", "").replace("商家", "")
        seller_time = seller_info[0]
        seller_type = seller_info[1:3]

        str3 = browser.find_element_by_css_selector("a div+div div span").text
        car_price = set_car_price(str3)
    # 翻页
    browser.find_element_by_id("listpagination").find_element_by_link_text("下一页").click()

# browser.find_element_by_id("listpagination").find_element_by_link_text("下一页").click()
# time.sleep(3)
# browser.quit()

