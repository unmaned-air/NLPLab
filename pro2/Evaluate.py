import string
#Q&A
'''
Q1: 词表
Q2：评价对于空格

'''
#计算几个参数：
#分子
#correct=0
#分母
#total1=0
#分母二
#total2=0
'''
    if str1 in str2:
        那么可能出现某一个词被分成了几个词，应该长词序列不动，继续向下滑动一格，继续判定
    
    
 '''
def Delete_character(str):
    c=str.replace(']','')
    c=c.replace('[','')
    c=c.replace('\'','')
    c=c.replace('\n','')
    c=c.replace(' ','')
    c=c.replace("\"",'')
    c=c.replace("，",'')
    c=c.replace("。",'')
    c = c.split(',')
    return str
with open('Cut1.txt','r',encoding='utf-8') as f1:
    # 分子
    correct = 0
    # 分母
    total1 = 0
    # 分母二
    total2 = 0
    with open('Cut_own2.txt','r',encoding='utf-8') as f2:
        a=f1.readline()#读取jieba分词的某个句子
        b=f2.readline()#读取
        while a and b:
            a=eval(a)
            b=eval(b)
            total1=total1+len(b)
            total2=total2+len(a)
            correct=correct+len(b)-len(set(b).difference(a))
            a = f1.readline()
            b = f2.readline()
P=correct/total1
R=correct/total2
F=(P+R)/(2*P*R)
print(f'准确率 {P}')
print(f'召回率 {R}')
print((f'F {F}'))

'''
不删除数字：
准确率 0.9455349813007389
召回率 0.9270774330874856
F 1.0681304405148933

数字删除后：
准确率 0.8406148397183137
召回率 0.9056636397784389
F 1.1468840727598308

'''