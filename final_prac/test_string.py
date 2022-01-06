# 奔驰GLC 2017款 GLC 260 4MATIC 豪华型
# str1 = "奔驰GLC 2017款 GLC 260 4MATIC 豪华型"
# car_class = ""
# car_launch_time = 2020
# car_style = ""
# car_drive_mode = ""
# car_type = ""
# is_AMG = 0
# had_refit = 0
# is_import = 0
# if "AMG" in str1:
#     is_AMG = 1
# 5万公里／2017-05／上海／2年钻石商家
str2 = "5万公里／2017-05／上海／2年钻石商家"
mileage = 5 * 10000
release_year = 2022
release_month = 7
release_area = ""
seller_time = 2
seller_type = ""

# 26.98万 √
def set_car_price(car_price):
    return int(float(car_price.replace("万", "")) * 10000)