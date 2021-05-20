from utils.dbutils import *


'''
返回：字典，uid为key，看过的内容id列表为value
'''
def get_user_items(table_name):
    sql = 'select `用户`,`索引` from %s'%table_name
    result = select_data(sql)
    data = {}
    for i in result:
        data.setdefault(str(i['用户']),[])
        data[str(i['用户'])].append(str(i['索引']))
    # print(data)
    return dict(data)


def get_item_base_data(table_name):
    """
    :return: 用户行为数据,dict,key为vid,value也为dict( key为uid, value=1)
    """
    pre_data = get_user_items(table_name)
    vid_list = []
    for i in pre_data.values():
        vid_list+=i
    vid_list = list(set(vid_list))
    data = {}
    for vid in vid_list:
        data.setdefault(vid,{})
        for uid,itemids in pre_data.items():
            for itemid in  itemids:
                if itemid == vid:
                    data[vid][uid] = 1
    return data

def get_user_base_data(table_name):
    """
    :return: 用户行为数据,dict,key为uid,value也为dict( key为vid, value=1)
    """
    pre_data = get_user_items(table_name)
    data = {}
    for i,items in pre_data.items():
        items_dict = {}
        for j in items:
            items_dict[j] = 1
        data.setdefault(i,items_dict.copy())
    return data


if __name__ == '__main__':
    # artical_action/scenery_action
    print('文章行为')
    artical_item_base_data = get_item_base_data('artical_action')
    artical_user_base_data = get_user_base_data('artical_action')
    print(artical_item_base_data)
    print(artical_user_base_data)
    print('景点行为')
    scenery_item_base_data = get_item_base_data('scenery_action')
    scenery_user_base_data = get_user_base_data('scenery_action')
    print(get_item_base_data('scenery_action'))
    print(get_user_base_data('scenery_action'))