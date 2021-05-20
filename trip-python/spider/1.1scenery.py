#!/usr/bin/env python
# coding: utf-8
'''
景点爬虫，从某个具体的地点开始
'''


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Firefox()

def to_one_place_detali(place):  # 进入一个地区的详情页
    url = 'http://www.mafengwo.cn/search/q.php?q='+place
    driver.get(url)
    elements = driver.find_elements_by_class_name('head-link')
    url = ''
    for i in elements:
        if '热门景点' in i.text:
            url = i.find_element_by_tag_name('a').get_attribute('href')
            break
    print(url)
    driver.get(url)


def get_one_place_all_jd(place):  # 获取一个地方所有景点信息
    all_data = []
    while True:
        time.sleep(1)
        elements = driver.find_element_by_class_name('scenic-list').find_elements_by_tag_name('li')
        for i in elements:
            url = i.find_element_by_tag_name('a').get_attribute('href')
            title = i.find_element_by_tag_name('a').get_attribute('title')
            img = i.find_element_by_tag_name('img').get_attribute('src')
            one_data = dict(zip(['url','title','img','location'],[url,title,img,place]))
            all_data.append(one_data)
#             print(one_data)
        try:
            driver.find_element_by_class_name('pg-next').click()
        except:
            return all_data


if __name__ == '__main__':
    place_list = ['武汉','长沙','丽江','香格里拉']
    all_data = []
    for i in place_list:
        to_one_place_detali(i)
        data = get_one_place_all_jd(i)
        all_data+=data
    df = pd.DataFrame(all_data)
    df.to_excel('景点信息.xls',index=False)





