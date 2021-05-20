#!/usr/bin/env python
# coding: utf-8
'''
文章爬虫，从某个景点开始
'''


from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Firefox()

def get_one_place_detali(place):  # 进入一个地区的详情页
    url = 'http://www.mafengwo.cn/search/q.php?q='+place
    driver.get(url)
    elements = driver.find_element_by_class_name('_j_search_section').find_elements_by_tag_name('li')
    all_data = []
    for i in elements:
        try:
            img = i.find_element_by_tag_name('img').get_attribute('src')
        except:
            continue
        url = i.find_element_by_tag_name('a').get_attribute('href')
        title = i.find_element_by_class_name('head').text
        content = i.find_element_by_class_name('content').text
        info = i.find_elements_by_class_name('seg-info')
        send_time = info[0].text
        views = info[1].text
        one_data = dict(zip(['url','img','title','content','send_time','views','place'],[url,img,title,content,send_time,views,place]))
        print(one_data)
        all_data.append(one_data)
    return all_data

if __name__ == '__main__':
    place_list = ['黄鹤楼','昙华林','归元禅寺','宝通禅寺','橘子洲景区','岳麓书院','马王堆汉墓','古开福寺','武汉大学','华中农业大学','华中师范大学','华中科技大学','东湖樱花园','东湖梅园','金银湖湿地公园','武汉海昌极地海洋公园']
    all_data = []
    for i in place_list:
        all_data+=get_one_place_detali(i)
    df = pd.DataFrame(all_data)
    df.to_excel('游记信息.xls',index=False)





