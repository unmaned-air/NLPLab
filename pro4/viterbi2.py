
from collections import Counter
import pandas as pd
num=400000
#测试集
'''
文件中的emission transfer来自于pro3中的输出结果
'''

dic2 = pd.read_table(r'emission.csv', sep=',', encoding='utf-8', low_memory=False)
dic2 = dic2.set_index('Unnamed: 0')

dic1 = pd.read_table(r'transfer.csv', sep=',', encoding='utf-8', low_memory=False)
dic1 = dic1.set_index('Unnamed: 0')
with open('first.txt', 'r', encoding='utf-8') as f2:
    dic3 = eval(f2.read())
with open('xtest.txt','r',encoding='utf-8') as f3:
    words=eval(f3.read())



class Path:
    def __init__(self, pre, now):
        self.pre = pre
        self.now = now


def Data_frame(dic):
    for i in dic.columns:
        for j in dic.index:
            if not pd.isna(dic[i][j]):
                dic[i][j] = eval(dic[i][j])
                dic[i][j] = dic[i][j][0] / dic[i][j][1]
            # else:
            #     dic[i][j] = 1/num

            # 让分子分母矩阵变成小数矩阵：是否会有精度的缺失？


Data_frame(dic1)
Data_frame(dic2)
for i in dic3.keys():
    dic3[i] = dic3[i][0] / dic3[i][1]


def label(dic):  # 输入的矩阵应该是df[词性][词语]
    dic = pd.DataFrame(dic.T)
    words = dic.columns
    word = dict(Counter(words))
    for j in words:
        c = []
        for i in dic.index:
            if not pd.isna(dic[j][i]):
                c.append(i)
        word[j] = c
    return word  # 得到词：词性选项的字典


word = label(dic2)


def max_(path_, s, i):
    p = -1
    j=0
    for j in range(len(path_)):
        p = max(p, path_[j][0] * dic1[path_[j][1]][s] * dic2[s][i])
    return (p, s, j)


def Veterbi(sentence):
    '''
    dic1:转移概率
    dic2:发射概率
    dic3:初始概率
    sentence：分好词的句子
    构造最大序列
    中心思想：更新权重，找到最短路径,如何实现是一个难题
    '''

    path = []  # 简化为三步法
    path_word = []
    for i in word[sentence[0]]:  # 第一个词的词性
        if i in dic3.keys():
            path.append((dic3[i], i))
    # 得到初始的矩阵
    for i in sentence:
        if len(sentence)==1:
            break
        path1 = []
        path2 = []
        for s in word[i]:
            path_ = max_(
                path, s, i
            )  # 第二层每一个词性当前步骤的最大权重
            path2.append(Path(path[path_[2]][1], path_[1]))
            '''
            如何取出路径？
            '''
            path1.append((path_[0], path_[1]))  # 用一个数组存储
        path = path1[:]  # 这几行代码想了几个小时md
        path_word.append(path2)
    last1 = -1
    last2 = (last1, 0)
    for i in range(len(path)):
        last1 = max(path[i][0], last1)
        if last1 != last2[0]:
            last2 = path[i]
    last = last2
    now = last[1]  # 当前的词性
    path_word.reverse()
    real_path = []
    real_path.append(now)
    for i in range(len(path_word)-1):
        for j in path_word[i]:
            if j.now == now:  # 找到之前词性
                now = j.pre
                real_path.append(now)
                break
    real_path.reverse()

    return real_path

path_all_word = []
skip=[]
for i in range(len(words)):
    try:
        path_all_word.append(Veterbi(words[i]))
    except:
        print(i)
        skip.append(i)
        path_all_word.append([])


with open('path_all_word2.txt', 'w', encoding='utf-8') as f3:
    f3.write(str(path_all_word))
with open('skip_sentence.txt','w',encoding='utf-8') as f4:
    for i in skip:
        f4.write(str(words[i]))
with open('skip.txt','w',encoding='utf-8') as f4:
    f4.write(str(skip))
