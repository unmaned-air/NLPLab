import string

with open('Old_ID.txt','r',encoding='utf-8') as f1:
    with open('new_ID.txt','r',encoding='utf-8') as f2:

        a=f1.readline().split(':')[1].strip('\'')
        b=f2.readline().split(':')[2].strip('\'')
        #print(f2.readline().split(':'))
        a=a.split(',')
        b=b.split(',')
        #print(a)
        #print(b)
        for i in range(len(b)):
            if b[i] in a:
                continue
            else:
                print(b[i])
