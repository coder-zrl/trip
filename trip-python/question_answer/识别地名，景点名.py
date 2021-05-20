import pandas as pd
import jieba
import jieba.posseg as pseg
jieba.enable_paddle()

def get_per_list(text):
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


if __name__ == '__main__':
    while 1:
        text = input()
        per_list = get_per_list(text)
        print(per_list)
