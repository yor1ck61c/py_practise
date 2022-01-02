import time
import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.maximize_window()
url = "https://movie.douban.com/top250"
browser.get(url)
browser.maximize_window()
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', '0601', 'localhost', '3306', 'db_python'))

movie_list = []
director_list = []
leading_role_list = []
release_time_list = []
type_list = []
grade_list = []
comment_num = []
movie_description_list = []

# 开始操作
for i in range(10):
    trs = browser.find_element_by_css_selector('ol.grid_view').find_elements_by_tag_name('li')
    for tr in trs:
        movie_list.append(tr.find_element_by_css_selector('div div+div div a span.title').text)
        # 所有信息
        info = tr.find_element_by_css_selector('div div+div div+div p').text
        # 导演
        director_list.append(info.split('...')[0].split('  主演:')[0][4:])
        # 主演
        try:
            protagonist = info.split('...')[0].split('  主演: ')[1]
        except Exception as e:
            protagonist = str(e)
        leading_role_list.append(protagonist)
        # 年份
        release_time_list.append(info.split('...')[-1].split(' / ')[0])
        # 类型
        type_list.append(info.split('...')[-1].split(' / ')[2])
        # 评分
        grade_list.append(tr.find_element_by_css_selector('div div+div div+div p+div span+span.rating_num').text)
        # 评论数
        comment_num.append(tr.find_element_by_css_selector('div div+div div+div p+div span+span+span+span').text[:-3])
        # 描述
        try:
            description = tr.find_element_by_css_selector('div div+div div+div p+div+p span.inq').text
        except Exception as e:
            description = str(e)
        movie_description_list.append(description)
    try:
        browser.find_element_by_css_selector('span[class="next"]').click()
    except Exception as e:
        print(str(e) + '已经到最后一页了')


df_write = pd.DataFrame({
    "movie_list": movie_list,
    "director_list": director_list,
    "leading_role_list": leading_role_list,
    "release_time_list": release_time_list,
    "type_list": type_list,
    "grade_list": grade_list,
    "comment_num": comment_num,
    "movie_describe_list": movie_description_list
})
df_write.to_sql("douban_Top250_movie_info", engine)
