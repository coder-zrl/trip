import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:422518@localhost:3306/3chuang')



# 新冠肺炎数据存入数据库
table_name = ['景点信息-分类后.xls','用户景点行为.xls','游记信息-分类后.xls','用户游记行为.xls','所有关系.xls']
file_name = ['scenery','scenery_action','artical','artical_action','relationship']
for i,j in zip(table_name,file_name):
    df = pd.read_excel(i)
    df.to_sql(j, engine,if_exists='replace')

