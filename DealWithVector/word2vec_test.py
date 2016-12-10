#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import gensim.models.doc2vec as Doc2Vec
# model = Doc2Vec.load_word2vec_format('../vectors.bin', binary=True)

from gensim.models import Word2Vec as wv

import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = wv.Text8Corpus(u"../txtfiles/split.txt")  # load input files
model = wv.Word2Vec(sentences,size=200)  # 训练skip-gram模型; 默认window=5

# 计算两个词的相似度/相关程度
y1 = model.similarity(u"不错", u"好")
print u"【不错】和【好】的相似度为：", y1
print "--------\n"

# 计算某个词的相关词列表
y2 = model.most_similar(u"质量", topn=20)  # 20个最相关的
print u"和【书】最相关的词有：\n"
for item in y2:
    print item[0], item[1]
print "--------\n"

# 寻找对应关系
print u"书-不错，质量-"
y3 = model.most_similar([u'质量', u'不错'], topn=3)
for item in y3:
    print item[0], item[1]
print "--------\n"

# 对应的加载方式
# model_2 = word2vec.Word2Vec.load("text8.model")

# 以一种C语言可以解析的形式存储词向量
model.save_word2vec_format(u"review.model.bin", binary=True)
# 对应的加载方式
# model_3 = word2vec.Word2Vec.load_word2vec_format("text8.model.bin", binary=True)

if __name__ == "__main__":
    pass
