from selenium import webdriver
browser = webdriver.Chrome(executable_path='/driver/chromedriver.exe')

browser.get("https://www.bilibili.com/v/popular/history")
browser.maximize_window()
lists = browser.find_element_by_css_selector('ul div.card-list').find_elements_by_css_selector("div.video-card")
count = 0
for data in lists:
    count += 1
    print("第{}个视频".format(count))
    title = data.find_element_by_css_selector("div+div p.video-name").text
    up_name = data.find_element_by_css_selector("div+div div span.up-name span").text
    play_times = data.find_element_by_css_selector("div+div div p.video-stat span.play-text").text
    float_comments = data.find_element_by_css_selector("div+div div p.video-stat span.play-text").text
    comment = data.find_element_by_css_selector("div+div div span.history-hint span").text
    print("标题:{},up主:{},播放量:{},弹幕量:{},评论:{}".format(title, up_name, play_times, float_comments, comment))
