# coding:utf-8
from py2neo import Graph, Node, Relationship
import pandas as pd

# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='zhang123321')
print('连接成功')



node_list = []
# 创建景点结点
print('正在创建景点节点')
sceneryname_node_map = {}
df1 = pd.read_excel('景点信息-分类后.xls')
for i in df1.index:
    one_data = df1.loc[i]
    node = Node('scenery',label='scenery', name=one_data['title'],img=one_data['img'],
                location=one_data['location'],classification=one_data['classification'],
                url=one_data['url'])
    sceneryname_node_map[one_data['title']] = node
    node_list.append(node)
# 创建游记节点
print('正在创建游记节点')
articalname_node_map = {}
df2 = pd.read_excel('游记信息-分类后.xls')
for i in df2.index:
    one_data = df2.loc[i]
    node = Node('artical', label='artical', title=one_data['title'],img=one_data['img'],
                content=one_data['content'], sendtime=one_data['send_time'],
                views=one_data['views'],scenery=one_data['place'],
                classification=one_data['classification'],
                url=one_data['url'])
    articalname_node_map[one_data['title']] = node
    node_list.append(node)
# 创建地区节点
print('正在创建地区节点')
placename_node_map = {}
place_list = ['武汉','长沙','丽江','香格里拉']
for i in place_list:
    node = Node('place',label='place', name=i)
    placename_node_map[i] = node
    node_list.append(node)



relationship_list = []
# 景点与景点之间的关系
print('正在创建景点与景点之间的关系')
df = pd.read_excel('关系——景点景点之间的关系.xls')
for i in df.index:
    one_data = df.loc[i]
    relationship = Relationship(sceneryname_node_map[one_data['A']], one_data['relationship'], sceneryname_node_map[one_data['B']])
    relationship_list.append(relationship)

# 景点与游记之间的关系
print('正在创建景点与游记之间的关系')
df = pd.read_excel('关系——游记景点之间的关系.xls')
for i in df.index:
    one_data = df.loc[i]
    relationship = Relationship(sceneryname_node_map[one_data['A']], one_data['relationship'], articalname_node_map[one_data['B']])
    relationship_list.append(relationship)

# 地区与景点之间的关系
print('正在创建地区与景点之间的关系')
df = pd.read_excel('关系——地区景点之间的关系.xls')
for i in df.index:
    one_data = df.loc[i]
    relationship = Relationship(sceneryname_node_map[one_data['A']], one_data['relationship'], placename_node_map[one_data['B']])
    relationship_list.append(relationship)


# 创建节点
[graph.create(i) for i in node_list]
print('所有节点创建完成')
# 创建关系
[graph.create(i) for i in relationship_list]
print('所有关系创建完成')

print(graph)
# print(test_node_1)
# print(test_node_2)
# print(node_1_zhangfu_node_1)
# print(node_2_qizi_node_1)
# print(node_2_munv_node_1)