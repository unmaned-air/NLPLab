from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
import jieba
from gensim.models import KeyedVectors
sen={}
feature={}
x=[]
target=[]

with open('w2vmodel/sentence.txt',encoding='utf-8')as f1:
    with open('w2vmodel/features.txt')as f2:
        sentence=f1.readline()
        features=f2.readline()
        while sentence:
            sentence=sentence.split('\t')
            features=features.split('\t')
            feature[features[0]]=eval(features[2].replace('\n',''))
            sen[sentence[0]]=sentence[2].replace('\n','')
            x.append(eval(features[2].replace('\n','')))
            target.append(eval(features[1]))
            sentence = f1.readline()
            features = f2.readline()

x_train,x_test,y_train,y_test=train_test_split(x,target,test_size=0.2,random_state=20)
print(len(x_test))
print(len(x_train))
#print(y_test)
model=LogisticRegression(random_state=20).fit(x_train,y_train)

#决定系数R^2

y_predict=model.predict(x_test)
#print(y_predict)
with open('result/W2V.txt','w',encoding='utf-8')as f3:
    f3.write(f'R^2 score:{model.score(x_test,y_test)}\n')
    f3.write(f'准确率：{accuracy_score(y_test,y_predict)}\n')
    #corect/total
    f3.write(f'精准率：{precision_score(y_test,y_predict)}\n')
    #TP/(TP+FP)
    f3.write(f'recall:{recall_score(y_test,y_predict)}\n')
    #TP/(TP+FN)
    f3.write(f'F_score:{f1_score(y_test,y_predict)}\n')
    #2(pre*recal)/(pre+recall)

sen=input('输入一句话：')
sen=jieba.lcut(sen)
model1 = KeyedVectors.load_word2vec_format('w2vmodel/skip_gram.bin')
f=[]
tag=0
for i in sen:
    if tag==0:
        f=model1.get_vector(model1.key_to_index[i])
    else:
        ff=model1.get_vector(model1.key_to_index[i])
        for j in range(len(f)):
            f[j]=f[j]+ff[j]
result=model.predict([f])
print(result)