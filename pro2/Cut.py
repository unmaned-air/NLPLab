

#全局变量：储存所有的分词（二维数组）
all_cut=[]
max_size=25
with open('indexes.txt','r',encoding='utf-8') as f1:
#with open('dictionary.txt','r',encoding='utf-8') as f1:
    dic=f1.read()
def cut(str1):
    '''
    now_Word=word[0:max_size]--判越界
    while now_Word not in dic:
        if len==1:
            cut.append{now_word}
            break
    else:
        append word
        now_word=[0:len(now_word)-1]
    word=word[now:max]
    cut.append(now_word)
    return cut
    '''
    lenth = len(str1)
    word = str1
    cut = []
    i=0
    j=0
    while lenth > 0:
        if len(word) < max_size:
            now_Word = word
        else:
            now_Word = word[0:max_size]
        while now_Word not in dic:
            if len(now_Word) == 1:
                break
            now_Word = now_Word[0:len(now_Word)-1]
        j=len(now_Word)+j
        cut.append((i,j))#先取一个list，在读取的时候再作其他操作
        word = word[len(now_Word):]
        i=i+len(now_Word)
        lenth = len(word)
    return cut
with open('CDIAL-BIAS-race.txt','r',encoding='utf-8') as f2:
    a=f2.readline()
    with open('Cut_own1.txt', 'w', encoding='utf-8') as f3:
        while a:
            cuta=cut(a)
            #all_cut.append(cuta)
            a=f2.readline()
            f3.write(str(cuta)+'\n')
#with open('Cut_own.txt','w',encoding='utf-8') as f3:
#    f3.write(str(all_cut))
