import pandas as pd
import random
from utils.item_base import *
from utils.dbutils import *

df = pd.read_excel('景点信息-分类后.xls')
relationship = []

# # 位于
# for i in df.index:
#     relationship.append({'A':df.loc[i]['title'],'relationship':'位于','B':df.loc[i]['location']})
# print('位于',relationship)


# 附近
for i in df.index:
    count = 0
    index_list = list(df.index)
    random.shuffle(index_list)
    for j in index_list:
        if i!=j and df.loc[i]['location']==df.loc[j]['location']:
            count+=1
            relationship.append({'A':df.loc[i]['title'],'relationship':'附近','B':df.loc[j]['title']})
            if count>10:
                break
print('附近',relationship)


# 相似
item_cf = Item_CF('scenery_action')
id_title_dict = dict(zip(list(df.index),df['title']))
for i in df.index:
    id_list = item_cf.get_one_recommend(str(i))
    for j in id_list:
        # sql = 'select * from scenery where `index`=%s'%j
        # data = select_data(sql)
        relationship.append({'A': df.loc[i]['title'], 'relationship': '相似', 'B': id_title_dict[eval(j)]})
print('相似',relationship)


df = pd.DataFrame(relationship)
df.to_excel('关系——景点景点之间的关系.xls')