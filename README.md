RyanNLP:Toolkits for Chinese processing
---
RyanNLP是一个处理简体中文的类库，是受到[NLTK](https://github.com/nltk/nltk)、[结巴分词](https://github.com/fxsjy/jieba)、[SnowNLP](https://github.com/isnowfy/snownlp)的启发而写的。

目前常见的自然语言处理类库的针对语言都是英文，很少有处理中文的类库，即便是有，很多类库也不是开源的，这给我们学习和使用都造成了不便。

RyanNLP是一个多种功能合一的中文自然语言处理类库，其*Killer feature*主要包括*繁简转换*、*中文分词*、*词性标注*、*文本摘要*、*关键字提取*、*文本分类*、*情感分析* ，Ryan会一直完善下去！

RyanNLP可以自定义训练过程，其所有功能都会随着训练语料的完善而变的更好，欢迎大家用自己的语料训练，同时自带一个包含2w行分词文本，2w行标注语料，以及2w行注音语料，来进行内含模型的训练。

使用说明
---

```python
    import RyanNLP
    m = RyanNLP(u"本条目當前的標題「繁体中文」為暫定名稱，可能為原創、不准确或者具爭議性。")
    print m.simp            #"本条目当前的标题「繁体中文」为暂定名称，可能为原创、不准确或者具争议性。"
    
    m.docs = m.simp
    print m.comp            #"本条目當前的標題「繁体中文」為暫定名稱，可能為原創、不准确或者具爭議性。"
    
    m.docs = u"重复的完成繁重的任务"
    print m.spell           #"chong fu de wan cheng fan zhong de ren wu"
    
    m.docs = "ni hao bei jing"
    print m.gen         #"你好北京"
    
    m.docs = u"今天天气不错，挺风和日丽的。"
    print m.seg         #"今天 天气 不错 ， 挺 风和日丽 的 。"
    
    print m.tag         #[('今天',t)('天气',n)('不错',a),(',',w)('挺',d)('风和日丽',i)('的',u)('。',w)]
    
    

```

Feature
---
* 中文繁简互相转换
* 中文注音,注音成词(隐式马尔可夫)
* 中文分词([Character-Based Generative Model](http://aclweb.org/anthology//Y/Y09/Y09-2047.pdf))
* 词性标注([TnT Part-Of-Speech Tag](http://aclweb.org/anthology//A/A00/A00-1031.pdf))
* 文本摘要([TextRank 算法](http://acl.ldc.upenn.edu/acl2004/emnlp/pdf/Mihalcea.pdf))
* 关键词提取([TextRank 算法](http://acl.ldc.upenn.edu/acl2004/emnlp/pdf/Mihalcea.pdf))
* 文本分类(Naive Bayes 分类)
* 文本相似([BM25 similarity](http://en.wikipedia.org/wiki/Okapi_BM25))
* 情感分析
* TF-IDF

About training
---

License
---
MIT licensed
