
'''
构建基于logis回归模型分类
实验6中的VSM表示文本进行分类
实验七中word2vec
任意输入一句话对其进行基于word2vec的向量表示，进行分类输出

数据集进行划分，对同一批数据进行不同的文本表示方法，
输出分类准确率、召回率和F1值，比较两类表示方法的效果差异。
'''
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sklearn.linear_model
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
# class VSM:
#     def __init__(self,X,Y,sentence):
#         self.x=X
#         self.y=Y
#         self.sentence=sentence
#     def
'''
构建  index to sentence
     index to features 
'''
sen={}
feature={}
x=[]
target=[]

with open('VSM/sentences.txt',encoding='utf-8')as f1:
    with open('VSM/features.txt')as f2:
        sentence=f1.readline()
        features=f2.readline()
        while sentence:
            sentence=sentence.split('\t')
            features=features.split('\t')
            feature[features[0]]=eval(features[1].replace('\n',''))
            sen[sentence[0]]=sentence[1].replace('\n','')
            x.append(eval(features[1].replace('\n','')))
            if features[0].split('.')[0]=='neg':
                target.append(0)
            else:
                target.append(1)
            sentence = f1.readline()
            features = f2.readline()

x_train,x_test,y_train,y_test=train_test_split(x,target,test_size=0.2,random_state=20)
print(len(x_test))
print(len(x_train))
model=LogisticRegression(random_state=20).fit(x_train,y_train)

#决定系数R^2
print(model.score(x_test,y_test))
y_predict=model.predict(x_test)
with open('result/VSM.txt','w',encoding='utf-8')as f3:
    f3.write(f'R^2 score:{model.score(x_test,y_test)}\n')
    f3.write(f'准确率：{accuracy_score(y_test,y_predict)}\n')
    #corect/total
    f3.write(f'精准率：{precision_score(y_test,y_predict)}\n')
    #TP/(TP+FP)
    f3.write(f'recall:{recall_score(y_test,y_predict)}\n')
    #TP/(TP+FN)
    f3.write(f'F_score:{f1_score(y_test,y_predict)}\n')
    #2(pre*recal)/(pre+recall)