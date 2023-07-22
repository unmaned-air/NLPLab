import jieba
from collections import Counter

import numpy as np

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ID=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
c=[]
def count_num(str1, str2, num, now):
    b = str1.count(str2)
    num[now] = num[now] + b
    if b!=0:
        c=str1.split()[0]
        return c
    else:
        return 0


#输出ID号


with open('CDIAL-BIAS-race.txt', encoding='utf-8') as f1:
    str = f1.readline()
    with open('race.txt', 'r', encoding='utf-8') as f2:
        d = f2.readline().strip("\n")
        while d:
            c.append(d)
            d = f2.readline().strip("\n")
    while str:
        for i in range(15):
            id=count_num(str, c[i], arr, i)
            if id!=0:
                ID[i].append(id)
        str = f1.readline()

    with open('new_devide.txt', 'w', encoding='utf-8') as f3:
        for i in range(15):
            f3.write(f'#{c[i]}：{arr[i]}\n')
    with open('new_ID.txt','w',encoding='utf-8') as f4:
        for i in range(15):
            f4.write(f'ID:{c[i]}:{ID[i]}\n')

#统计的结果发现，不分词的词语比分过词的多多了，是因为分词的时候，可能会有某些词分在了一起