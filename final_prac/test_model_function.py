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


def set_second_string(second_str, mileage, release_year, release_month, release_area, seller_time, seller_type):
    infos = second_str.split('／')

    mileage = float(infos[0].replace("万公里", "")) * 10000

    date_info = infos[1].split('-')
    release_year = int(date_info[0])
    release_month = int(date_info[1])

    release_area = infos[2]

    seller_info = infos[3].replace("年", "").replace("商家", "")
    seller_time = seller_info[0]
    seller_type = seller_info[1:3]


def set_car_price(price):
    return int(float(price.replace("抢购价", "").replace("万", "")) * 10000)