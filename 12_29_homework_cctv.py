import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')

browser.get("https://tv.cctv.com/epg/index.shtml?spm=C31267.PFsKSaKh6QQC.EEfEAhEnQFPl.3")
browser.maximize_window()
# 3、抓取央视网(CCTV1-CCTV5)节目信息：时间、节目名称
cctv = browser.find_element_by_id("jiemudan01").find_elements_by_css_selector("div.channel_con div ul li")
for index in range(5):
    morningList = browser.find_element_by_id("jiemudan01").find_elements_by_css_selector("tbody#shangwu tr")
    afternoonList = browser.find_element_by_id("jiemudan01").find_elements_by_css_selector("tbody#xiawu tr")

    # 上午的节目
    print("cctv{}节目".format(index + 1))
    for i in morningList:
        name = i.find_element_by_css_selector("td.text span a").text
        date = i.find_element_by_css_selector("td.time i").text
        print("时间:{} 节目名:{}".format(date, name))
    # 下午的节目
    for i in afternoonList:
        name = i.find_element_by_css_selector("td.text span a").text
        date = i.find_element_by_css_selector("td.time i").text
        print("时间:{} 节目名:{}".format(date, name))
    time.sleep(2)
    cctv[index + 1].click()
    time.sleep(2)
