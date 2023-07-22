import jieba
from collections import Counter

str2=[]
ID=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]



def count_num(str1, str2):
    '''

    :param str1:
    :param str2:
    :return:
    注意并不是所有语句split之后都能规范的第一个元素是标号第二个元素是完整的语料串
    '''
    global ID
    c=str1[1]
    for i in range(2,len(str1)):
        c=c+str1[i]
    print(c)
    c=jieba.lcut(c)
    b = Counter(c)
    for i in range(15):
        if str2[i] in b.keys():
            ID[i].append(str1[0])




with open('race.txt',encoding='utf-8') as f2:
    d = f2.readline().strip("\n")
    while d:
        str2.append(d)
        d = f2.readline().strip("\n")
    print(str2)

jieba.suggest_freq(str2, True)
jieba.suggest_freq(('东南亚人'), True)


with open("CDIAL-BIAS-race.txt",encoding='utf-8') as f1:
    str1=f1.readline().split()
    while str1:
        #str1[1] = jieba.lcut(str1[1])
        #这里有问题
        if str1[0]=='5924':
            print(str1[2])
        #print(str1[0])
        count_num(str1,str2)
        str1 = f1.readline().split()


with open("Old_ID.txt",'w',encoding='utf-8') as f3:
    for i in range(15):
        f3.write(f'ID{str2[i]}:{ID[i]}\n')
#print(ID)
