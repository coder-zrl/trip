import json
import os
from math import sqrt



class User_CF():
    def __init__(self,filepath='./static/data/data2.json',user_sim_path='./static/data/user_sim.json'):
        self.filepath = filepath
        self.item_sim_path = user_sim_path
        self.action_data = self.load_action_data()

    # 加载用户行为数据,dict,key为uid,value也为dict( key为vid, value=1)
    def load_action_data(self,filename="./static/data/data1.json"):
        return json.load(open(filename,encoding='utf-8'))

    # 计算两个用户的余弦距离，余弦相似度。person1、person2, 用户1的点击记录,dict,key为视频id,value=1
    def cos_distance(self,person1, person2):
        dot_sum = 0
        for item in person1:
            if item in person2:
                dot_sum += person1[item] * person2[item]
        if 0 == len(person1) or 0 == len(person2):
            return 0
        else:
            score = float(dot_sum) / sqrt(len(person1) * len(person2) * 1.0)  # 向量元素值均为1
            return score

    # 为一个用户推荐视频
    def get_recommend(self, uid,times=1,num=10):
        score_sum = {}  # 记录视频的推荐得分,key为vid,value为对应的得分加和
        uid_action = self.action_data[uid]  # 推荐用户的点击记录
        # 遍历每一个用户,对相似的用户,获得推荐
        for other_uid in self.action_data:
            if uid == other_uid:  # 自己的不计算
                continue
            other_action = self.action_data[other_uid]  # 其他用户的行为数据
            sim_score = self.cos_distance(uid_action, other_action)
            # 如果没有任何相似,则不进行推荐
            if sim_score==0:
                continue
            # 对相似的用户,获得其浏览记录,以及对应的推荐得分
            for vid in other_action:
                if not vid in uid_action:  # 用户已经看过的视频不计算
                    score_sum.setdefault(vid, 0)
                    score_sum[vid] += sim_score * other_action[vid]  # 相似用户对该视频的推荐分
        # 获得最终的得分
        recommend_list = []
        for vid in score_sum:
            # final_score = float(score_sum[vid])/sim_sum[vid]
            final_score = score_sum[vid]
            recommend_list.append((vid, final_score))
        final_recommend_list = sorted(recommend_list, key=lambda d: d[1], reverse=True)  # 按照第二个关键字来排序，降序
        data = [i[0] for i in final_recommend_list]
        return data[(times-1)*num:times*num]


if __name__ == "__main__":
    user_cf = User_CF()
    vid_ls = user_cf.get_recommend('1')
    print(vid_ls)