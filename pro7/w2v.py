import torch
from gensim.models import word2vec
from gensim.models import Word2Vec
from collections import Counter
import math
# 读取数据
with open('data/neg.txt', encoding='utf-8') as f1:
    neg = eval(f1.read())
with open('data/pos.txt', encoding='utf-8') as f2:
    pos = eval(f2.read())
# w2v skip gram
vector_size = 64
window = 5
min_count = 3
epochs = 3
sg = 0
data=neg
data.extend(pos)

model1 = word2vec.Word2Vec(data, vector_size=vector_size, window=window,
                           epochs=epochs, sg=sg,hs=0, negative=5)
for i,k in enumerate(model1.wv.key_to_index):
    print(k)
model1.wv.save_word2vec_format('model/Cbow.bin')

# w2v skip
sg = 1
model2 = word2vec.Word2Vec(data, vector_size=vector_size, window=window,
                           epochs=epochs, sg=sg)
model2.wv.save_word2vec_format('model/skip_gram.bin')



