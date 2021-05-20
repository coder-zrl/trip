from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
from utils.dbutils import *
from utils.user_base import *
from utils.item_base import *
from question_answer.问题分类器 import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 登录,传一个uid
@app.route('/login')
def login():
    res = {}
    res['result'] = 'success'
    return jsonify(res)


# 注册,传一个uid
@app.route('/register')
def register():
    res = {}
    res['result'] = 'success'
    return jsonify(res)


# 推荐景点和游记,传一个uid
@app.route('/recommend',methods=['GET','POST'])
def recommend():
    uid = request.values.get('uid')
    res = {}
    # 先基于user
    user_cf = User_CF('scenery_action')
    id_list = user_cf.get_one_recommend(str(uid))[:3]
    # 再将第一个替换为item
    new_id_list = []
    for i in id_list:
        item_cf = Item_CF('scenery_action')
        new_id_list.append(item_cf.get_one_recommend(str(i))[0])
    scenery_data = []
    for i in id_list:
        sql = 'select * from scenery where `index`=%s' % i
        one_data = select_data(sql)[0]
        new_one_data = {}
        new_one_data['url'] = one_data['img']
        new_one_data['title'] = one_data['title']
        scenery_data.append(new_one_data)
    res['scenery'] = scenery_data

    # 先基于user
    user_cf = User_CF('artical_action')
    id_list = user_cf.get_one_recommend(str(uid))[:3]
    # 再将第一个替换为item
    new_id_list = []
    for i in id_list:
        item_cf = Item_CF('artical_action')
        new_id_list.append(item_cf.get_one_recommend(str(i))[0])
    artical_data = []
    for i in id_list:
        sql = 'select * from artical where `index`=%s' % i
        one_data = select_data(sql)[0]
        new_one_data = {}
        new_one_data['url'] = one_data['img']
        new_one_data['title'] = one_data['title']
        new_one_data['details'] = one_data['content']
        new_one_data['local'] = one_data['send_time'].split('/')[0].strip()
        new_one_data['time'] = one_data['send_time'].split('/')[0].strip()
        new_one_data['viewsNumber'] = one_data['views'].strip('浏览')
        new_one_data['islike'] = False
        artical_data.append(new_one_data)
    res['artical'] = artical_data
    return jsonify(res)


# 问答,传一个uid
@app.route('/qa',methods=['GET','POST'])
def hello_world():
    question = request.values.get('question')
    print(question)
    res = {}
    ans,nodes,links = question_classifier(question)
    res['ans'] = ans
    if len(nodes)==0:
        nodes.append({'id': 1,'category' : 0,'name' : '黄鹤楼', 'symbol' : 'circle','symbolSize' : 40})
        nodes.append({'id': 2, 'category': 0, 'name': '武汉大学', 'symbol': 'circle', 'symbolSize': 40})
        nodes.append({'id': 3, 'category': 1, 'name': '武汉', 'symbol': 'circle', 'symbolSize': 40})
        links.append({'source': 2, 'target': 1, 'value': '附近景点', 'name': '附近景点', })
        links.append({'source': 1, 'target': 3, 'value': '位于', 'name': '位于', })
    res['nodes'] = nodes
    res['links'] = links
    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
