from utils.item_base import *
from utils.user_base import *

'''
:param recommend_type: 推荐的类型，是item还是user
:param which: 是为景点推荐还是为游记推荐，在本项目中为为两个值scenery、artical
传入的table_name为scenery_action、artical_action
:param for_id: 为哪个推荐的id
:return: 
'''
def get_recommend(recommend_type,which,for_id):
    if recommend_type=='item':
        if which=='scenery' or which=='artical':
            item_cf = Item_CF('%s_action'%which)
            id_list = item_cf.get_one_recommend(str(for_id))
            return id_list
        else:
            print('暂无此类型数据')
    elif recommend_type=='user':
        if which=='scenery' or which=='artical':
            user_cf = User_CF('%s_action'%which)
            id_list = user_cf.get_one_recommend(str(for_id))
            return id_list
        else:
            print('暂无此类型数据')
    else:
        print('类型错误')

if __name__ == '__main__':
    data = get_recommend('user','artical',2)
    print(data)