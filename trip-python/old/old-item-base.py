import json
import os
from math import sqrt


class Item_CF():
    def __init__(self, filepath='./static/data/data1.json', item_sim_path='./static/data/item_sim.json'):
        self.filepath = filepath
        self.item_sim_path = item_sim_path
        self.item_sim = None
        self.action_data = self.load_action_data()

        self.load_action_data()
        if os.path.exists(self.item_sim_path):
            self.item_sim = json.load(open(self.item_sim_path, encoding='utf-8'))
        else:
            self.item_sim = self.get_all_sim_item()

    # 加载用户行为数据，dict,key为vid,value也为dict( key为uid, value=1)
    # 需要实时从数据库里找
    def load_action_data(self):
        return json.load(open(self.filepath, encoding='utf-8'))

    # 求皮尔逊相关系数
    def sim_pearson(self, p1, p2):
        # 得到双方都曾评价过的物品列表
        si = {item: 1 for item in p1 if item in p2}
        n = len(si)
        if n == 0:
            return 0
        # 对所有偏好求和
        sum1 = sum(p1[it] for it in si)
        sum2 = sum(p2[it] for it in si)
        # 求平方和
        sum1sq = sum(pow(p1[it], 2) for it in si)
        sum2sq = sum(pow(p2[it], 2) for it in si)
        # 求乘积之和
        pSum = sum(p1[it] * p2[it] for it in si)
        # 计算皮尔逊评价值
        num = pSum - (sum1 * sum2 / n)
        den = sqrt((sum1sq - pow(sum1, 2) / n) * (sum2sq - pow(sum2, 2) / n))
        if den == 0:
            return 0
        r = num / den
        return r

    # 计算的余弦距离，返回余弦相似度 item1、item2, dict,key为特征id,value=1
    def cos_distance(self, item1, item2):
        dot_sum = 0
        for item in item1:
            if item in item2:
                dot_sum += item1[item] * item2[item]
        if 0 == len(item1) or 0 == len(item2):
            return 0
        else:
            score = float(dot_sum) / sqrt(len(item1) * len(item2) * 1.0)  # 向量元素值均为1
            return score

    # 获取某两个物品的相似度
    def get_sim_item(self, vid):
        sim_video_list = []  # 记录视频的相似视频,内容为元组(vid视频id，sim相似度)
        vid_vsm = self.action_data[vid]  # 视频的用户向量表示
        # 遍历每一个视频，获得相似度
        for other_vid in self.action_data:
            if vid == other_vid:  # 自己的不计算
                continue
            other_vid_vsm = self.action_data[other_vid]  # 其他视频的向量表示
            sim_score = self.cos_distance(vid_vsm, other_vid_vsm)  # 求相似度
            sim_video_list.append([other_vid, sim_score])
        final_sim_list = sorted(sim_video_list, key=lambda d: d[1], reverse=True)
        # print(final_sim_list)
        # 格式化处理
        vid_vid2_sim = {}
        for vid2, score in final_sim_list:
            sim_data = {}
            sim_data["vid1"] = vid
            sim_data["vid2"] = vid2
            sim_data["sim"] = score
            if int(vid) < int(vid2):  # 相似度只记录一遍即可
                vid_vid2_sim[vid2] = score
        return vid_vid2_sim

    # 获取某物品与其他所有物品的相似度
    def get_all_sim_item(self):
        # 获得所有视频的相似视频,最多max_num个视频
        vid_vid_sim_data = {}
        for vid in self.action_data:
            vid_vid_sim_data[vid] = self.get_sim_item(vid)
        # print(vid_vid_sim_data)
        json.dump(vid_vid_sim_data, open(self.item_sim_path, 'w', encoding='utf-8'))
        return vid_vid_sim_data

    # 获取一个物品的推荐
    def get_one_recommend(self, vid, times=1, num=10):
        data = []
        if vid in self.item_sim:
            for i in list(self.item_sim[vid].items())[(times - 1) * num:times * num]:
                data.append(i[0])
        else:
            print('未发现物品id')
        return data


if __name__ == "__main__":
    item_cf = Item_CF()
    id_list = item_cf.get_one_recommend('1')
    print(id_list)
