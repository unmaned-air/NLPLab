import jieba

'''
重新分词，使用jieba写入文件成元组
'''
words=[]
with open('race.txt','r',encoding='utf-8') as f3:
    a = f3.readline()
    while a:
        words.append(a)
        a = f3.readline()
jieba.suggest_freq(words, True)
jieba.suggest_freq(('东南亚人'), True)

with open('Cut1.txt','w',encoding='utf-8') as f2:
    with open('CDIAL-BIAS-race.txt',encoding='utf-8') as f1:
    #print(str(f1.readline()).split())
        a=str(f1.readline())
        while a:
            c=jieba.lcut(str(a))
            index=[]
            j=0
            for i in range(len(c)):
                tup=(j,j+len(c[i]))
                j=j+len(c[i])
                index.append(tup)
            f2.write(str(index)+'\n')
            a = str(f1.readline())
