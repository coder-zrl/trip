import pandas as pd
import json
import random
random.seed(10)


df = pd.read_excel('景点信息.xls')

classification = []
index_dict = {'大学':[],'公园':[],'武汉':[],'长沙':[],'丽江':[],'香格里拉':[]}
for i in df.index:
    print(df.loc[i])
    if '大学' in df.loc[i]['title']:
        classification.append('大学')
        index_dict['大学'].append(i)

    elif '园' in df.loc[i]['title']:
        classification.append('公园')
        index_dict['公园'].append(i)

    else:
        classification.append(df.loc[i]['location'])
        index_dict[df.loc[i]['location']].append(i)
df['classification'] = classification
df.to_excel('景点信息-分类后.xls')


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
    else:
        [all_data.append({'用户': '5', '索引': j}) for j in i[1]]
    # 用户再一些其他类别地点
    [all_data.append({'用户': '5', '索引': j}) for j in random.sample(index_list,len(index_list)//20)]


df = pd.DataFrame(all_data)
df.to_excel('用户景点行为.xls')