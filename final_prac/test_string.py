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
infos = str2.split('／')

mileage = int(infos[0].replace("万公里", "")) * 10000

date_info = infos[1].split('-')
release_year = int(date_info[0])
release_month = int(date_info[1])

release_area = infos[2]

seller_info = infos[3].replace("年", "").replace("商家", "")
seller_time = seller_info[0]
seller_type = seller_info[1:3]

print(mileage)
print(release_year)
print(release_month)
print(release_area)
print(seller_time)
print(seller_type)

# 26.98万 √
# def set_car_price(car_price):
#     return int(float(car_price.replace("万", "")) * 10000)