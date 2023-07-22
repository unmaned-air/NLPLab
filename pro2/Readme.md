## pro2（实验二）的说明：

- Dictionary.py 获取词表

  其中输出了两个词表，第一个词表是未删除数字与部分字符的indexes.txt，第二个词表是删除数字的dictionary.txt

- Cut.py用于获取基于摘取的词表的正向最大匹配分词

  其中由两个词表分别输出了两个分词结果，第一个结果是基于indexes.txt的Cut_own.txt,第二个是基于dictionary.txt的Cut_own2.txt

- Evaluate.py用于分别计算基于新词表分词的两个结果的准确率，召回率，F测度，仅用print函数观测输出，并将输出附于程序最末的zhu'shi