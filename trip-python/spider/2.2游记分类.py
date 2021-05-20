import pandas as pd
import json
import random
random.seed(10)


df = pd.read_excel('游记信息.xls')

classification = []
index_dict = {'大学':[],'公园':[],'武汉':[],'长沙':[]}
for i in df.index:
    print(df.loc[i])
    if df.loc[i]['place'] in ['武汉大学','华中农业大学','华中师范大学','华中科技大学']:
        classification.append('大学')
        index_dict['大学'].append(i)
    elif df.loc[i]['place'] in ['东湖樱花园','东湖梅园','金银湖湿地公园','武汉海昌极地海洋公园']:
        classification.append('公园')
        index_dict['公园'].append(i)
    elif df.loc[i]['place'] in ['黄鹤楼','昙华林','归元禅寺','宝通禅寺']:
        classification.append('武汉')
        index_dict['武汉'].append(i)
    elif df.loc[i]['place'] in ['橘子洲景区','岳麓书院','马王堆汉墓','古开福寺']:
        classification.append('长沙')
        index_dict['长沙'].append(i)
df['classification'] = classification
df.to_excel('游记信息-分类后.xls')




json.dump(index_dict,open('分类情况.json','w',encoding='utf-8'),ensure_ascii=False)
index_list = []
for i in index_dict.values():
    index_list+=list(i)
all_data = []
for i in index_dict.items():
    if i[0] == '大学':
        [all_data.append({'用户':'1','索引':j}) for j in i[1]]
    elif i[0] == '公园':
        [all_data.append({'用户':'2','索引':j}) for j in i[1]]
    elif i[0] == '武汉':
        [all_data.append({'用户':'3','索引':j}) for j in i[1]]
    elif i[0] == '长沙':
        [all_data.append({'用户':'4','索引':j}) for j in i[1]]
    # 用户再一些其他类别地点
    [all_data.append({'用户': '5', '索引': j}) for j in random.sample(index_list,len(index_list)//20)]
df = pd.DataFrame(all_data)
df.to_excel('用户游记行为.xls')