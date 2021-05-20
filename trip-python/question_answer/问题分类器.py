import jieba
import jieba.posseg as pseg
from utils.dbutils import *
from question_answer.获取天气情况 import *
import re
from utils.user_base import *
jieba.enable_paddle()

def get_loc_list(text):
    per_list = []  # 人名列表
    word_list = jieba.lcut(text)
    # print(word_list)
    for word in word_list:
        if len(word)==1:  # 不加判断会爆
            continue
        words = pseg.cut(word, use_paddle=True)  # paddle模式
        # print(list(words))
        word, flag = list(words)[0]
        if flag=='LOC':  # 这里写成LOC是地名
            per_list.append(word)
    per_list = list(set(per_list))
    # print(per_list)
    return per_list

def question_classifier(text,uid='1'):
    # 如果flag一直为0的话就表示看不懂
    ans = '呜呜呜，我没看懂，换个问题试试'

    # 地区有什么景点
    if len(re.findall('.*?有什么好玩的.*?|.*?有哪些.*?景点',text))>0:
        print('地区有什么景点')
        all_data = []
        nodes = []
        links = []
        ner = get_loc_list(text)[0]
        sql = 'select * from scenery where location="%s" limit 10'%ner
        all_data = select_data(sql)
        ans = '、'.join([i['title'] for i in all_data])

        # 添加景点node
        index = 0
        for i in all_data:
            nodes.append({'id':index,'category':0,'name':i['title'],'symbol' : 'circle','symbolSize' : 40})
            index+=1
        # 添加地区node
            nodes.append({'id': index, 'category': 1, 'name': ner, 'symbol': 'circle', 'symbolSize': 40})
            index += 1

        # 添加关系
        for i in nodes:
            if i['category']==0:
                links.append({'source': i['id'], 'target': index-1, 'value': '位于', 'name': '位于'})

        return ans,nodes,links

    # 景点在哪个地区
    if len(re.findall('(.*?)在哪里|(.*?)在什么地方|(.*?)在哪儿|(.*?)在.*?|(.*?)在哪座城市',text))>0:
        print('景点在哪个地区')
        all_data = []
        nodes = []
        links = []
        ner = get_loc_list(text)[0]
        sql = 'select location from scenery where title="%s"'%ner
        all_data = select_data(sql)[0]
        ans = all_data['location']

        # 两个node
        nodes.append({'id': 1, 'category': 0, 'name': ner, 'symbol': 'circle', 'symbolSize': 40})
        nodes.append({'id': 2, 'category': 0, 'name': ans, 'symbol': 'circle', 'symbolSize': 40})
        links.append({'source': 1, 'target': 2, 'value': '位于', 'name': '位于'})
        return ans,nodes,links
        # print('景点在哪个地区')

    # 地区、景点的气候
    if len(re.findall('.*?天气.*?|.*?这几天的天气.*?|.*?这几天的天气预报|.*?最近的天气预报|.*?今天的天气怎么样|.*?今天的天气如何',text))>0:
        print('地区、景点的气候')
        nodes = []
        links = []
        ner = get_loc_list(text)[0]
        # 判断是地区还是景点，如果是景点就找到地区
        sql = 'select * from scenery where title="%s" limit 10'%ner
        if len(select_data(sql)):
            sql = 'select location from scenery where title="%s"'%ner
            ner = select_data(sql)[0]['location']
        data = get_weather(ner)['data']['forecast'][0]
        ans = '、'.join([data['type'],data['high'],data['low'],data['fengxiang']])
        return ans,nodes,links

    # 附近景点
    if len(re.findall('.*?附近有什么景点.*?|.*?附近有哪些景点.*?|.*?附近.*?景点.*?',text))>0:
        print('附近景点')
        all_data = []
        nodes = []
        links = []
        ner = get_loc_list(text)[0]
        sql = 'select * from relationship where A="%s" and relationship="%s" limit 10'%(ner,'附近')
        all_data = select_data(sql)
        ans = '、'.join([i['B'] for i in all_data])

        index = 0
        for i in all_data:
            nodes.append({'id': index, 'category': 0, 'name': i['B'], 'symbol': 'circle', 'symbolSize': 40})
            index+=1
        nodes.append({'id': index, 'category': 0, 'name': all_data[0]['A'], 'symbol': 'circle', 'symbolSize': 40})
        index+=1
        # 联系
        for i in nodes:
            if i['name']!= all_data[0]['A']:
                links.append({'source': i['id'], 'target': index-1, 'value': '附近', 'name': '附近'})
        return ans,nodes,links
        # print('附近景点')

    # 相似景点
    if len(re.findall('.*?相似的景点.*?|.*?类似的景点.*?',text))>0:
        print('相似景点')
        all_data = []
        nodes = []
        links = []
        ner = get_loc_list(text)[0]
        sql = 'select * from relationship where A="%s" and relationship="%s" limit 10'%(ner,'相似')
        all_data = select_data(sql)
        ans = '、'.join([i['B'] for i in all_data])

        index = 0
        for i in all_data:
            nodes.append({'id': index, 'category': 0, 'name': i['B'], 'symbol': 'circle', 'symbolSize': 40})
            index+=1
        nodes.append({'id': index, 'category': 0, 'name': all_data[0]['A'], 'symbol': 'circle', 'symbolSize': 40})
        index+=1
        # 联系
        for i in nodes:
            if i['name']!= all_data[0]['A']:
                links.append({'source': i['id'], 'target': index-1, 'value': '相似', 'name': '相似'})

        return ans,nodes,links

        # print('相似景点')

    # # 景点相关的vlog
    # if len(re.findall('.*?相关的视频.*?|.*?黄鹤楼相关的vlog.*?',text))>0:
    #     ans = '景点相关的vlog'
    #     # print('景点相关的vlog')

    # 景点相关的游记
    if len(re.findall('.*?相关的游记.*?',text))>0:
        print('景点相关的游记')
        all_data = []
        nodes = []
        links = []
        ner = get_loc_list(text)[0]
        sql = 'select * from relationship where A="%s" and relationship="%s" limit 3' % (ner, '相关游记')
        # print(sql)
        all_data = select_data(sql)
        # print(data)
        ans = '、\n'.join([i['B'] for i in all_data])

        index = 0
        for i in all_data:
            nodes.append({'id': index, 'category': 2, 'name': i['B'], 'symbol': 'circle', 'symbolSize': 40})
            index+=1
        nodes.append({'id': index, 'category': 0, 'name': all_data[0]['A'], 'symbol': 'circle', 'symbolSize': 40})
        index+=1
        # 联系
        for i in nodes:
            if i['name']!= all_data[0]['A']:
                links.append({'source': i['id'], 'target': index-1, 'value': '相关游记', 'name': '相关游记'})
        return ans,nodes,links

    # 推荐景点
    if len(re.findall('.*?推荐一些景点|推荐景点',text))>0:
        print('推荐景点')
        all_data = []
        nodes = []
        links = []
        user_cf = User_CF('scenery_action')
        id_list = user_cf.get_one_recommend(uid)
        for i in id_list:
            sql = 'select * from scenery where `index`=%s'%i
            one_data = select_data(sql)[0]
            all_data.append(one_data)
        ans = '、'.join([i['title'] for i in all_data])

        index = 0
        for i in all_data:
            nodes.append({'id': index, 'category': 0, 'name': i['title'], 'symbol': 'circle', 'symbolSize': 40})
            index+=1
        return ans,nodes,links


    # 推荐游记
    if len(re.findall('.*?推荐一些游记|推荐游记',text))>0:
        print('推荐游记')
        all_data = []
        nodes = []
        links = []
        user_cf = User_CF('artical_action')
        id_list = user_cf.get_one_recommend(uid)[:3]
        for i in id_list:
            sql = 'select * from artical where `index`=%s'%i
            one_data = select_data(sql)[0]
            all_data.append(one_data)
        ans = '、\n'.join([i['title'] for i in all_data])

        index = 0
        for i in all_data:
            nodes.append({'id': index, 'category': 2, 'name': i['title'], 'symbol': 'circle', 'symbolSize': 40})
            index+=1
        return ans,nodes,links

    # # 推荐vlog
    # if len(re.findall('.*?推荐一些视频|推荐视频|.*?推荐一些vlog|推荐vlog',text))>0:
    #     ans = '推荐vlog'
    #     # print('推荐vlog')
    return ans,[],[]


if __name__ == '__main__':
    while 1:
        text = input('问:')
        ans = question_classifier(text)
        print('分类结果:',ans)
    '''
    问:黄鹤楼在哪座城市
    分类结果: 景点在哪个地区
    问:武汉的天气怎么样
    分类结果: 地区、景点的气候
    问:和黄鹤楼相关的游记
    分类结果: 景点相关的游记
    问:武汉有哪些景点
    分类结果: 地区有什么景点
    问:和黄鹤楼类似的景点有哪些
    分类结果: 相似景点
    问:黄鹤楼附近有哪些景点
    分类结果: 附近景点
    问:推荐一些视频
    分类结果: 推荐vlog
    '''