from collections import Counter

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
    with open('race.txt','r',encoding='utf-8') as f2:
        c = c.split(',')
        b = dict(Counter(c))
        d = f2.readline().strip("\n")
        with open('frequency.txt','w',encoding='utf-8') as f3:
            while d:
                f3.write(f'#{d} : {b[d]} \n ')
                d = f2.readline().strip("\n")