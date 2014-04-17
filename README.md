RyanNLP:Toolkits for Chinese processing
---
RyanNLP是一个处理简体中文的类库，是受到[NLTK](https://github.com/nltk/nltk)、[结巴分词](https://github.com/fxsjy/jieba)、[SnowNLP](https://github.com/isnowfy/snownlp)的启发而写的。

目前常见的自然语言处理类库的针对语言都是英文，很少有处理中文的类库，即便是有，很多类库也不是开源的，这给我们学习和使用都造成了不便。

RyanNLP是一个多种功能合一的中文自然语言处理类库，其*Killer feature*主要包括*繁简转换*、*中文分词*、*词性标注*、*文本摘要*、*关键字提取*、*文本分类*、*情感分析* ，Ryan会一直完善下去！

RyanNLP可以自定义训练过程，其所有功能都会随着训练语料的完善而变的更好，欢迎大家用自己的语料训练，同时自带一个包含2w行分词文本，2w行标注语料，以及2w行注音语料，来进行内含模型的训练。

使用说明
---

RyanNLP可以在Python解释器中运行,也可以方便的包含在Python程序中,以下给出Python解释器中的各个功能的API的调用过程。

```python

    import RyanNLP
    test = u"""自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言， 所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言， 而在于研制能有效地实现自然语言通信的计算机系统， 特别是其中的软件系统。
因而它是计算机科学的一部分。
重复完成繁重的任务。 """

    m = RyanNLP(test)

    print test

    print "------Spell----"
    print m.spell
    print

    print "------Comple---"
    print m.comp
    print

    print "------Segs-----"
    m.words
    print

    print "------Tags-----"
    m.tags
    print

    print "------keyWords-"
    m.keyWords
    print

    print "------Abstract-"
    m.extractSentence
    print

    print "------"

    
```

The result is 

```python
    自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言， 所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言， 而在于研制能有效地实现自然语言通信的计算机系统， 特别是其中的软件系统。
因而它是计算机科学的一部分。
重复完成繁重的任务。 
------Spell----
zi ran yu yan chu li shi ji suan ji ke xue ling yu yu ren gong zhi neng ling yu zhong de yi ge zhong yao fang xiang 。 
ta yan jiu neng shi xian ren yu ji suan ji zhi jian yong zi ran yu yan jin xing you xiao tong xin de ge zhong li lun he fang fa 。 
zi ran yu yan chu li shi yi men rong yu yan xue 、 ji suan ji ke xue 、 shu xue yu yi ti de ke xue 。 
yin ci ， zhe yi ling yu de yan jiu jiang she ji zi ran yu yan ， ji ren men ri chang shi yong de yu yan ，   suo yi ta yu yu yan xue de yan jiu you zhao mi qie de lian xi ， dan you you zhong yao de qu bie 。 
zi ran yu yan chu li bing bu shi yi ban di yan jiu zi ran yu yan ，   er zai yu yan zhi neng you xiao di shi xian zi ran yu yan tong xin de ji suan ji xi tong ，   te bie shi qi zhong de ruan jian xi tong 。 
yin er ta shi ji suan ji ke xue de yi bu fen 。 
chong fu wan cheng fan zhong de ren wu 。

------Comple---
自然語言處理是計算機科學領域與人工智能領域中的一個重要方嚮。
它研究能實現人與計算機之間用自然語言進行有效通信的各種理論和方法。
自然語言處理是一門融語言學、計算機科學、數學於一體的科學。
因此，這一領域的研究將涉及自然語言，即人們日常使用的語言， 所以它與語言學的研究有著密切的聯繫，但又有重要的區彆。
自然語言處理併不是一般地研究自然語言， 而在於研製能有效地實現自然語言通信的計算機繫統， 特彆是其中的軟件繫統。
因而它是計算機科學的一部分。
重複完成繁重的任務。

------Segs-----
自然 语言 处理 是 计算机 科学 领域 与 人工 智能 领域 中 的 一个 重要 方向
它 研究 能 实现 人 与 计算机 之间 用 自然 语言 进行 有效 通信 的 各种 理论 和 方法
自然 语言 处理 是 一 门融 语言 学 、 计算机 科学 、 数学 于 一体 的 科学
因此 ， 这 一 领域 的 研究 将 涉及 自然 语言 ， 即 人们 日常 使用 的 语言 ，   所以 它 与 语言学 的 研究 有着 密切 的 联系 ， 但 又 有 重要 的 区别
自然 语言 处理 并 不 是 一般 地 研究 自然 语言 ，   而 在于 研制 能 有效 地 实现 自然 语言 通信 的 计算机 系统 ，  特别 是 其中 的 软件 系统
因而 它 是 计算机 科学 的 一 部分
重复 完成 繁重 的 任务

------Tags-----
自然/n 语言/n 处理/v 是/v 计算机/n 科学/n 领域/n 与/c 人工/b 智能/n 领域/n 中/f 的/u 一个/m 重要/a 方向/n
它/r 研究/v 能/v 实现/v 人/n 与/p 计算机/n 之间/f 用/v 自然/a 语言/n 进行/v 有效/a 通信/vn 的/u 各种/r 理论/n 和/c 方法/n
自然/n 语言/n 处理/v 是/v 一/m 门融/q 语言/n 学/v 、/w 计算机/n 科学/n 、/w 数学/n 于/p 一体/n 的/u 科学/n
因此/c ，/w 这/r 一/m 领域/n 的/u 研究/vn 将/d 涉及/v 自然/a 语言/n ，/w 即/v 人们/n 日常/b 使用/vn 的/u 语言/n ，/w  /c 所以/c 它/r 与/p 语言学/a 的/u 研究/vn 有着/v 密切/a 的/u 联系/vn ，/w 但/c 又/d 有/v 重要/a 的/u 区别/n
自然/n 语言/n 处理/vn 并/c 不/d 是/v 一般/a 地/u 研究/vn 自然/n 语言/n ，/w  /r 而/c 在于/v 研制/v 能/v 有效/a 地/u 实现/v 自然/n 语言/n 通信/vn 的/u 计算机/n 系统/n ， /k 特别/d 是/v 其中/r 的/u 软件/n 系统/n
因而/c 它/r 是/v 计算机/n 科学/n 的/u 一/m 部分/m
重复/vd 完成/v 繁重/a 的/u 任务/n

------keyWords-
研究自然语言 自然语言 计算机 语言

------Abstract-
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言， 所以它与语言学的研究有着密切的联系，但又有重要的区别
自然语言处理并不是一般地研究自然语言， 而在于研制能有效地实现自然语言通信的计算机系统， 特别是其中的软件系统
自然语言处理是一门融语言学、计算机科学、数学于一体的科学

------
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
