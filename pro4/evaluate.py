
with open('ytrain.txt','r',encoding='utf-8') as f1:
    with open('path_all_word1.txt','r',encoding='utf-8') as f2:
        Y=eval(f1.read())
        Y_=eval(f2.read())
        correct=0
        total=0
        for i in range(len(Y)):
            correct=correct+len(Y[i])-len(set(Y[i]).difference(Y_[i]))
            total=total+len(Y[i])
        acc=correct/total
print(acc)
#0.9900250255542632
with open('skip.txt','r',encoding='utf-8') as f:
    skip=eval(f.read())
with open('ytest.txt','r',encoding='utf-8') as f1:
    with open('path_all_word2.txt','r',encoding='utf-8') as f2:
        Y=eval(f1.read())
        Y_=eval(f2.read())
        correct=0
        total=0
        for i in range(len(Y)):
            if i in skip:
                continue#此处有跳跃两条无法标注词性的句子
            correct=correct+len(Y[i])-len(set(Y[i]).difference(Y_[i]))
            total=total+len(Y[i])
        acc=correct/total
print(acc)
#0.9896855187206258