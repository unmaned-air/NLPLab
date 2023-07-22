import jieba
from jieba import posseg as ps

from sklearn.model_selection import train_test_split
from collections import Counter
import pandas as pd
import csv
from zhon import hanzi
import re
import copy

puntuation = r',|\.|\;|\?|\!|。|；|！|？'

words = []
indexes = []
j=0
with open('CDIAL-BIAS-race.txt',encoding='utf-8') as f1:
    txt=f1.readline()
    while txt:
        j=j+1
        #print(j)
        txt=re.split(puntuation,txt)
        for i in range(len(txt)):
            if txt[i]=='':
                continue
            c=ps.cut(txt[i])
            rec=[]
            inderec=[]
            for i in c:
                rec.append(i.word)
    #print('hh'+i.word)
                inderec.append(i.flag)
            words.append(rec[:])#words不需要tuple?
            indexes.append(inderec[:])#是这个细节的问题吗？
        txt=f1.readline()
    #d=ps.lcut(txt)

with open('cut_ci.txt','w',encoding='utf-8') as f2:
    for i in range(len(words)):
        f2.write(str(words[i]))
        f2.write(str(indexes[i]))

x_train,x_test,y_train,y_test= train_test_split(words,indexes,test_size=0.2)
with open('xtrain.txt','w',encoding='utf-8') as f3:
    f3.write(str(x_train))
with open('ytrain.txt','w',encoding='utf-8') as f3:
    f3.write(str(y_train))
with open('xtest.txt','w',encoding='utf-8') as f3:
    f3.write(str(x_test))
with open('ytest.txt','w',encoding='utf-8') as f3:
    f3.write(str(y_test))

# 初始状态概率
y_train_copy = []
for i in range(len(y_train)):
    if x_train[i][0] == '\n':
        continue
    elif len(x_train[i]) == 1 and x_train[i][0].isdigit():
        print(x_train[i])
        continue
    elif x_train[i][0].isdigit():
        cop = []
        cop = copy.deepcopy(y_train[i])
        # print(x_train[i])
        # print(cop)
        cop.pop(0)
        cop.pop(0)
        # print(cop)
        y_train_copy.append(cop)
        continue
    y_train_copy.append(y_train[i])

# print(first)
# 一句一句要考虑

first=[]
white=0
for i in range(len(y_train_copy)):
#     print(i)
    try:
        first.append(y_train_copy[i][0])
    except:
        white=white+1
        print(y_train_copy[i])
lenth=len(y_train_copy)-white
dic1=dict(Counter(first))
index1=list(dic1.keys())

for i in index1:
    dic1[i]=(dic1[i],lenth)
with open('first.txt','w',encoding='utf-8') as f3:
    f3.write(str(dic1))
#相邻词性二元组
pron=[]
for i in range(len(y_train)):
    for j in range(len(y_train[i])-1):
        pron.append((y_train[i][j],y_train[i][j+1]))

dic2=dict(Counter(pron))
key=list(dic2.keys())#提取二元组词典的索引
first2=[]
for i in range(len(key)):
    first2.append(key[i][0])#提取索引（元组）中的首元素
dic_first=dict(Counter(first2))#计数（其实是在生成一个字典）
for i in dic_first.keys():#在首元素的索引中进行提取 相邻词性二元组中，第一个词性是q_1的二元组个数
    dic_first[i]=0#归零字典的值
    for j in key:
        if j[0]==i:#如果第一个元素是这个
            dic_first[i]=dic_first[i]+dic2[j]#加上二元组的数量

matrix=pd.DataFrame(columns=list(dic_first.keys()),index=list(dic_first.keys()))#转移矩阵
#[q1]->[q2]

for i in list(dic2.keys()):
    matrix[i[0]][i[1]]=(dic2[i],dic_first[i[0]])
#matrix.to_csv('transfer.txt', sep=' ', index=True,header=True,quoting=csv.QUOTE_NONE,escapechar=' ')
matrix.to_csv('transfer.csv')#直接保存为csv
# 词-词性二元组
emission=[]
a=list(words)
for i in range(len(words)):
    for j in range(len(words[i])):
        emission.append((words[i][j],indexes[i][j]))
dic3=dict(Counter(emission))

col=[]
ind=[]
for i in dic3.keys():
    col.append(i[0])
    ind.append(i[1])

col=dict(Counter(col))
ind=dict(Counter(ind))
matrix_emission=pd.DataFrame(index=col.keys(),columns=ind.keys())

key=list(dic3.keys())#提取二元组词典的索引
second=[]
for i in range(len(key)):
    second.append(key[i][1])#提取索引（元组）中的第二个元素
print(key[i][1])
dic_second=dict(Counter(second))#计数（其实是在生成一个字典）
for i in dic_second.keys():
    dic_second[i]=0
    for j in dic3.keys():
        if j[1]==i:
            dic_second[i]=dic_second[i]+dic3[j]
for i in dic3.keys():#在首元素的索引中进行提取 相邻词性二元组中，第一个词性是q_1的二元组个数
    matrix_emission[i[1]][i[0]]=(dic3[i],dic_second[i[1]])#词-词性
    #保存分子分母
#matrix_emission.to_csv('emission.txt', sep=' ', index=True,header=True,quoting=csv.QUOTE_NONE,escapechar=' ')
matrix_emission.to_csv('emission.csv')