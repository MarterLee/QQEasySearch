# 简易版的搜索引擎

QQEasySearch 是一个能够支持扩展的建议搜索框架，支持正则搜素和向量搜索，并支持对搜索结果进行展示优化。
## 模块介绍

### data
    data模块实现数据的预处理与入库操作
### match 
    match模块实现从数据库中对已经处理好的数据进行召回，召回操作通常在数据中按一定的相关性和规则进行粗略的备选item进行大量的检索。
### rank
    rank模块对召回后的item进行排序，并截断出一个较小的数量。
### mix
    mix模块是可有可无的，若按rank排序生成推荐结果，可能会产生item的base地点过于分散，价格过高或过低，mix模块通过一些策略实现基于地理位置，item属性的排序打乱，以实现特定的透出效果。

## 安装需要的模块
### spaCy 的英文版本 按照自己的电脑系统参考：https://spacy.io/usage
    pip install -U pip setuptools wheel
    pip install -U 'spacy[apple]'
    python -m spacy download en_core_web_trf
### gensim 
    pip install gensim

### 向量检索库 Faiss
    conda install -c pytorch faiss-cpu
