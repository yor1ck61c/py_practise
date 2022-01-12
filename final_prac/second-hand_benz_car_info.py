import time
import numpy as np
import pandas as pd
from selenium import webdriver
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', '0601', 'localhost', '3306', 'py_final_work'))
browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.maximize_window()
# 窗口最大化
url = "https://www.che168.com/china/benchi/"
# 加载需要访问的地址
browser.get(url)
# 开始操作
# 定义变量
car_class_list = []
car_launch_time_list = []
car_drive_mode_list = []
is_AMG_list = []
mileage_list = []
release_year_list = []
release_month_list = []
release_area_list = []
seller_time_list = []
seller_type_list = []
car_price_list = []


# 定义函数
def set_car_price(price):
    return int(float(price.replace("抢购价", "").replace("万", "")) * 10000)


# range(x), 取前x页数据。总数据量为 105 + 56(x-1) 个
for i in range(100):
    time.sleep(1)
    car_infos = browser.find_element_by_id("goodStartSolrQuotePriceCore0").find_elements_by_css_selector("ul li")
    for j in range(len(car_infos)-1):
        car_class = ""
        car_launch_time = 2020
        car_drive_mode = "后驱"
        is_AMG = 0
        mileage = 0
        release_year = 0
        release_month = 0
        release_area = "长沙"
        seller_time = 0
        seller_type = "无"
        car_price = 0
        str1 = car_infos[j].find_element_by_css_selector("a div+div h4").text
        if "奔驰" not in str1:
            continue
        else:
            if "AMG" in str1:
                is_AMG = 1
                is_AMG_list.append(is_AMG)
                str1 = str1.replace("AMG", "")
            else:
                is_AMG_list.append(is_AMG)
            if "改" in str1:
                str1 = str1.replace("改款", "")
            if "进" in str1:
                str1 = str1.replace("(进口)", "")
            if "4MATIC" in str1:
                car_drive_mode = "4MATIC"
                car_drive_mode_list.append(car_drive_mode)
                str1 = str1.replace("4MATIC", "")
            else:
                car_drive_mode_list.append(car_drive_mode)
            if "轿跑" in str1:
                str1 = str1.replace("轿跑", "")
            if "新能源" in str1:
                str1 = str1.replace("新能源", "")
            infos = str1.split(" ")
            car_class = infos[0].replace("奔驰", "").replace("级", "")
            car_class_list.append(car_class)
            car_launch_time = infos[1].replace("款", "")
            car_launch_time_list.append(car_launch_time)
        str2 = car_infos[j].find_element_by_css_selector("a div+div p").text
        infos = str2.split('／')

        mileage = int(float(infos[0].replace("万公里", "")) * 10000)
        mileage_list.append(mileage)

        date_info = infos[1]
        if date_info == "未上牌":
            release_year_list.append(release_year)
            release_month_list.append(release_month)
        else:
            date_info = date_info.split('-')
            release_year = int(date_info[0])
            release_month = int(date_info[1])
            release_year_list.append(release_year)
            release_month_list.append(release_month)

        release_area = infos[2]
        release_area_list.append(release_area)

        seller_info = infos[3].replace("年", "").replace("商家", "")
        if len(seller_info) > 0:
            seller_time = seller_info[0]
            seller_type = seller_info[1:3]
            seller_time_list.append(seller_time)
            seller_type_list.append(seller_type)
        else:
            seller_time_list.append(seller_time)
            seller_type_list.append(seller_type)
        str3 = car_infos[j].find_element_by_css_selector("a div+div div span").text
        car_price = set_car_price(str3)
        car_price_list.append(car_price)
        # print(car_class, car_launch_time, car_drive_mode, is_AMG, had_refit, is_import,
        #       mileage, release_year, release_month, release_area, seller_time, seller_type, car_price)

    # 翻页
    browser.find_element_by_id("listpagination").find_element_by_link_text("下一页").click()

print(len(car_class_list))
print(len(car_launch_time_list))
print(len(car_drive_mode_list))
print(len(is_AMG_list))
print(len(mileage_list))
print(len(release_year_list))
print(len(release_month_list))
print(len(release_area_list))
print(len(seller_time_list))
print(len(seller_type_list))
print(len(car_price_list))


df_write = pd.DataFrame({
    "car_class": car_class_list,
    "car_launch_time": car_launch_time_list,
    "car_drive_mode": car_drive_mode_list,
    "is_AMG": is_AMG_list,
    "mileage": mileage_list,
    "release_year": release_year_list,
    "release_month": release_month_list,
    "release_area": release_area_list,
    "seller_time": seller_time_list,
    "seller_type": seller_type_list,
    "car_price": car_price_list
})
df_write.index = np.arange(1, len(df_write)+1)
df_write.to_sql("second_hand_benz_data", engine)
time.sleep(5)
browser.quit()
