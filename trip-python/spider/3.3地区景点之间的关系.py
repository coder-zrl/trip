import pandas as pd
import random
from utils.item_base import *
from utils.dbutils import *

df = pd.read_excel('景点信息-分类后.xls')
relationship = []

# 包含景点
for i in df.index:
    relationship.append({'A':df.loc[i]['title'],'relationship':'位于','B':df.loc[i]['location']})
print('包含景点',relationship)



df = pd.DataFrame(relationship)
df.to_excel('关系——地区景点之间的关系.xls')