import jieba
from gensim.models import Word2Vec, KeyedVectors, word2vec
from collections import Counter
import numpy as np
import math

'''
step1：获取词向量 √
step2：计算tfidf（按啥获取词向量？？？）
step3：归一化
'''
vector_size=64
# skip__gram
model1 = KeyedVectors.load_word2vec_format('model/skip_gram.bin')
print('skip gram')
print(model1.get_vector(model1.key_to_index[input()]))

# Cbow
model2 = KeyedVectors.load_word2vec_format('model/Cbow.bin')
print('Cbow')
print(model2.get_vector(model2.key_to_index[input()]))

dict1 = model1.key_to_index
dict2 = model2.key_to_index

def Tf_IDf(sentence,total,dict):
    '''

    :param sentence:
    :param feature:
    :param ind: 0->dict1 1->dict2
    :return: features
    '''
    dic1 = Counter(sentence)
    features = {}
    for i in dic1.keys():
        try:
            tf = dic1[i] / len(sentence)
            idf = math.log(total / dict[i], 2)
            features[i] = tf * idf
        except:
            continue
    # tf idf
    return features

data=[]
with open('tfidf/sentences.txt', encoding='utf-8') as f1:
    sen=f1.readline()
    while sen:
        sen=sen.replace('\n','')
        data.append(sen.split('\t'))
        sen=f1.readline()

def softmax(v):
    v1={}
    v11=[]
    for i in v.keys():
        v1[i]=math.exp(v[i])
        v11.append(v1[i])
    sum1=sum(v11)
    for i in v.keys():
        v1[i]=v1[i]/sum1
    return v1

total=len(data)
def status(sentence, dic):
    dic_ = {}
    for i in sentence:
        if i in dic_:
            continue
        else:
            dic_[i] = 1
    for i in dic_.keys():
        if i in dic.keys():
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

for i in range(len(data)):
    data[i][1]=jieba.lcut(data[i][1])
dic={}
for i in range(len(data)):
    status(data[i][1],dic)
def ft(sentence,a):
    '''
    :param sentence: 句子
    :param a: 权重
    :return:
    '''
    feature=[0]*vector_size
    for i in sentence:
        try:
            v=list(model1.get_vector(model1.key_to_index[i]))
            for j in range(len(v)):
                v[j]=v[j]*a[i]
                feature[j]=feature[j]+v[j]
        except:
            continue
    return feature


##取skip
with open('r_features.txt','w')as f3:
    with open('sentence.txt','w',encoding='utf-8')as f4:
        tag=1
        id=0
        for i in data:
            id=id+1
            v = Tf_IDf(i[1],total,dic)
            a=softmax(v)
            feature=ft(i[1],a)
            tag=i[0].split('.')[0]
            if tag=='neg':
                tag=0
            else:
                tag=1
            f3.write(f'{id}\t{tag}\t{feature}\n')
            str1=''.join(i[1])
            f4.write(f'{id}\t{tag}\t{str1}\n')
        # tag=0
        # for i in neg:
        #     id=id+1
        #     v = Tf_IDf(i,total,dic)
        #     a=softmax(v)
        #     feature=ft(i,a)
        #     f3.write(f'{id}\t{tag}\t{feature}\n')
        #     str1=''.join(i)
        #     f4.write(f'{id}\t{tag}\t{str1}\n')
