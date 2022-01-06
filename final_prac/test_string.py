# # 奔驰GLC 2017款 GLC 260 4MATIC 豪华型
# car_class = ""
# car_launch_time = 2020
# car_drive_mode = ""
# is_AMG = 0
# had_refit = 0
# is_import = 0


# def set_first_string(str1, car_class, car_launch_time, car_drive_mode, is_AMG, had_refit, is_import):
#     if "AMG" in str1:
#         is_AMG = 1
#         str1.replace("AMG", "")
#     if "改" in str1:
#         had_refit = 1
#         str1.replace("改款", "")
#     if "进" in str1:
#         is_import = 1
#         str1.replace("(进口)", "")
#     if "4MATIC" in str1:
#         car_drive_mode = "4MATIC"
#         str1.replace("4MATIC", "")
#     infos = str1.split(" ")
#     car_class = infos[0].replace("奔驰", "").replace("级", "")
#     car_launch_time = infos[1].replace("款", "")

# 5万公里／2017-05／上海／2年钻石商家 √
def set_second_string(str2, mileage, release_year, release_month, release_area, seller_time, seller_type):         
    infos = str2.split('／')

    mileage = int(infos[0].replace("万公里", "")) * 10000

    date_info = infos[1].split('-')
    release_year = int(date_info[0])
    release_month = int(date_info[1])

    release_area = infos[2]

    seller_info = infos[3].replace("年", "").replace("商家", "")
    seller_time = seller_info[0]
    seller_type = seller_info[1:3]
    # print(mileage)
    # print(release_year)
    # print(release_month)
    # print(release_area)
    # print(seller_time)
    # print(seller_type)

str2 = "5万公里／2017-05／上海／2年钻石商家 √"
mileage = 0
release_year = 2000
release_month = 6
release_area = "长沙"
seller_time = 2022
seller_type = ""
set_second_string(str2, mileage, release_year, release_month, release_area, seller_time, seller_type)
print(mileage)
print(release_year)
print(release_month)
print(release_area)
print(seller_time)
print(seller_type)


# 26.98万 √
# def set_car_price(car_price):
#     car_price = int(float(car_price.replace("万", "")) * 10000)