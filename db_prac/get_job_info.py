import time
import pandas as pd
from selenium import webdriver
from sqlalchemy import create_engine

browser = webdriver.Chrome(executable_path='C:/Users/ASUS/PycharmProjects/py_practise/driver/chromedriver.exe')
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', '0601', 'localhost', '3306', 'db_python'))

# 窗口最大化
url = "https://search.51job.com/list/020000%252C010000%252C030200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
# 加载需要访问的地址
browser.get(url)
browser.maximize_window()
# 开始操作
time.sleep(3)
# 岗位名称
job_name_list = []
# 日期
release_date_list = []
# 薪资
salary_list = []
# 地区
work_area_list = []
# 经验年限
work_experience_list = []
# 学历
edu_background_list = []
# 招聘人数
employ_nums = []
# 公司名称
company_name_list = []
job_info_list = browser.find_element_by_class_name("j_result").find_elements_by_class_name("e")
for job_info in job_info_list:
    job_name_list.append(job_info.find_element_by_css_selector("a p span").text)
    date = job_info.find_element_by_css_selector("a p span+span").text
    release_date_list.append(date.replace("发布", ""))
    salary_list.append(job_info.find_element_by_css_selector("a p+p span").text)
    info_list = job_info.find_element_by_css_selector("a p+p span+span").text.split("|")
    work_area_list.append(info_list[0])
    work_experience_list.append(info_list[1])
    edu_background_list.append(info_list[2])
    employ_nums.append(info_list[3])
    company_name_list.append(job_info.find_element_by_class_name("er").find_element_by_css_selector("a").text)
df_write = pd.DataFrame({
    "job_name_list": job_name_list,
    "release_date_list": release_date_list,
    "salary_list": salary_list,
    "work_area_list": work_area_list,
    "work_experience_list": work_experience_list,
    "edu_background_list": edu_background_list,
    "employ_nums": employ_nums,
    "company_name_list": company_name_list
    })
df_write.to_sql("job_info", engine)
time.sleep(5)
browser.quit()
