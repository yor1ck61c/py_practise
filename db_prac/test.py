import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
browser.get('https://movie.douban.com/top250')
browser.maximize_window()  # 最大化
time.sleep(2)
for i in range(10):
    print("------------第{}页数据------------".format(i + 1))
    trs = browser.find_element_by_css_selector('ol.grid_view').find_elements_by_tag_name('li')
    for tr in trs:
        name = tr.find_element_by_css_selector('div div+div div a span.title').text
        # 所有信息
        info = tr.find_element_by_css_selector('div div+div div+div p').text
        # 导演
        director = info.split('...')[0].split('  主演:')[0][4:]
        # 主演
        try:
            protagonist = info.split('...')[0].split('  主演: ')[1]
        except Exception as e:
            protagonist = str(e)
        # 年份
        year = info.split('...')[-1].split(' / ')[0]
        # 国家
        country = info.split('...')[-1].split(' / ')[1]
        # 类型
        move_type = info.split('...')[-1].split(' / ')[2]
        # 评分
        score = tr.find_element_by_css_selector('div div+div div+div p+div span+span.rating_num').text
        # 评论数
        describe_people = tr.find_element_by_css_selector('div div+div div+div p+div span+span+span+span').text[:-3]
        # 描述
        try:
            description = tr.find_element_by_css_selector('div div+div div+div p+div+p span.inq').text
        except Exception as e:
            description = None
        print('电影名称：{}，导演：{}，主演：{}，年份：{}，国家：{}，类型：{}，评分：{}，评论数：{}，描述：{}'.format(name, director, protagonist, year,
                                                                                country, move_type, score,
                                                                                describe_people, description))
    try:
        browser.find_element_by_css_selector('span[class="next"]').click()
    except Exception as e:
        print('已经到最后一页了')
