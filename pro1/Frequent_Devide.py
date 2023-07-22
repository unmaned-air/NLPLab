import jieba

words=[]
with open('race.txt','r',encoding='utf-8') as f3:
    a = f3.readline()
    while a:
        words.append(a)
        a = f3.readline()
jieba.suggest_freq(words, True)
jieba.suggest_freq(('东南亚人'), True)

jieba.suggest_freq(('\t'), True)
with open('Cut.txt','w',encoding='utf-8') as f2:
    with open('CDIAL-BIAS-race.txt',encoding='utf-8') as f1:
    #print(str(f1.readline()).split())
        a=str(f1.readline())
        while a:
            c=jieba.lcut(str(a))
            f2.write(str(c)+'\n')
            a = str(f1.readline())

