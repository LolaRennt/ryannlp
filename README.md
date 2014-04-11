RyanNLP:A tool kits for simplified Chinese processing
===
RyanNLP是一个处理简体中文的类库，是受到SnowNLP的启发而写的。RyanNLP内置训练数据，并且可以自行针对需要进行训练，可以自行定制，提高功能准确性。

大多数自然语言处理库都是针对英文的，而针对中文的自然语言处理类库比较少，而且功能比较单一。RyanNLP是一个包含多种功能的自然语言处理类库，主要包括繁简转换、中文分词、词性标注、文本摘要、关键字提取、文本分类等功能，目前仍在不断完善。

Features
===
* 中文分词
* 词性标注(Tnt part of speech tag)
* 文本分类(Naive bayes)
* 繁-简-拼音转换
* 提取文本关键字(TextRank算法）
* 文本摘要（TextRank算法）
* tf-idf

How to use
===

```
    import RyanNLP
    m = RyanNLP(u"本条目當前的標題「繁体中文」為暫定名稱，可能為原創、不准确或者具爭議性。 ... 注意：本條目可能有部分字元無法顯示，")
    print m.simp 
    #本条目当前的标题「繁体中文」为暂定名称，可能为原创、不准确或者具争议性。 ... 注意：本条目可能有部分字元无法显示，
    
    m.docs = u"重复的完成繁重的任务"
    print m.spell
    #chong fu de wan cheng fan zhong de ren wu
    
    m.docs = "ni hao bei jing"
    print m.gen
    #你好北京
    
    m.docs = u"今天天气不错，挺风和日丽的。"
    print m.seg
    #今天 天气 不错 ， 挺 风和日丽 的 。
    
    print m.tag
    #[(今天,t)(天气,n)(不错,a),(,,w)(挺,d)(风和日丽,i)(的,u)(。,w)]
    
    

```


About training
===

License
===
MIT licensed
