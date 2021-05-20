import pandas as pd
import random
from utils.item_base import *
from utils.dbutils import *

df = pd.read_excel('游记信息-分类后.xls')
relationship = []

# 景点相关游记
for i in df.index:
    relationship.append({'A':df.loc[i]['place'],'relationship':'相关游记','B':df.loc[i]['title']})
print('相关游记',relationship)


df = pd.DataFrame(relationship)
df.to_excel('关系——游记景点之间的关系.xls')