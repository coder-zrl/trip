import pandas as pd

file_list = ['关系——地区景点之间的关系.xls','关系——景点景点之间的关系.xls','关系——游记景点之间的关系.xls']
df_list = [pd.read_excel(i) for i in file_list]

relationship = []
for i in df_list:
    for j in i.index:
        relationship.append({'A':i.loc[j]['A'],'relationship':i.loc[j]['relationship'],'B':i.loc[j]['B']})
df = pd.DataFrame(relationship)
df.to_excel('所有关系.xls')