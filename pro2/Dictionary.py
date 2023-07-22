from collections import Counter
import zhon.hanzi


#对原分词结果进行预处理，获取词表
with open('Cut.txt','r',encoding='utf-8') as f:
    a=f.read()
    #print()
    c=a.replace(']','')
    c=c.replace('[','')
    c=c.replace('\'','')
    c=c.replace('\n','')
    c=c.replace(' ','')
    c=c.replace("\"",'')
    c=c.replace("，",'')
    c=c.replace("。",'')
    c=c.replace("\\n",'')
    c = c.split(',')
    b = dict(Counter(c))

b.pop('')

b=dict(sorted(b.items(), key=lambda x: x[1], reverse=True))
dic=list(b.keys())
print(dic)
print(len(max(dic,key=len,default='')))
#25
with open('indexes.txt','w',encoding='utf-8') as f1:
    for i in range(len(dic)):
        f1.write(dic[i]+'\n')
with open('dictionary.txt','w',encoding='utf-8') as f2:
    for i in range(len(dic)):
        if dic[i].isdigit():
            continue
        if dic[i] in zhon.hanzi.punctuation:
            continue
        f2.write(dic[i]+'\n')


#过拟合


