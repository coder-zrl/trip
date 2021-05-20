import json



def get_item_base_data():
    """
    :return: 用户行为数据,dict,key为vid,value也为dict( key为uid, value=1)
    """
    pre_data = get_user_items(False)
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
    json.dump(data, open('data1.json', 'w', encoding='utf-8'))

def get_user_base_data():
    """
    :return: 用户行为数据,dict,key为uid,value也为dict( key为vid, value=1)
    """
    pre_data = get_user_items(False)
    data = {}
    for i,items in pre_data.items():
        items_dict = {}
        for j in items:
            items_dict[j] = 1
        data.setdefault(i,items_dict.copy())
    json.dump(data, open('data2.json', 'w', encoding='utf-8'))



# data = {}
# for line in open('ratings.dat'):
#     userid, itemid, record, _ = line.split('::')
#     if eval(userid)>50:
#         break
#     data.setdefault(userid,{})
#     data[userid][itemid] = 1



'''
返回：字典，uid为key，看过的内容id列表为value
'''
def get_user_items(write=True):
    data = {}
    for line in open('ratings.dat'):
        userid, itemid, record, _ = line.split('::')
        if eval(userid)>50:
            break
        data.setdefault(userid,[])
        data[userid].append(itemid)
    if write:
        json.dump(data,open('data3.json','w',encoding='utf-8'))
    return data


if __name__ == '__main__':
    get_user_items()