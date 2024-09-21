# dialects-io-be

this is the backend!!

### functional requirements

* 搜索
    * 用户输入发音搜寻
        * 汉语拼音
        * 其他拼音
    * 用户输入常用汉字搜索
    * 用户输入正字搜索
    * 以后可以支持按照意思搜索（成本略高，需要向量数据库），甚至chatbot

* 显示
    * 字，按照正体字，显示 
        * 常用写法，以及为什么简化至此，甚至网络用语
        * 所有发音，以及该发音的来源（上山下乡带来的绍兴发音）
        * 组词，可以点击词进入词的页面
        * 意思（支持多语言）
        * 出处，可以点击进入出处页面
    * 词，按照正体词，显示
        * 所有发音
        * 常用写法
        * 意思（支持多语言）
        * 造句
        * 出处，可以点击进入出处页面
        * 用户可以点击每个字进入字的页面
    * 出处，可以显示该文献信息

* 信息录入
    * 必须登录，后端核实为contributor

### database design

* 标准字表 (standard_forms)

    * 意思和发音会被存入另外的表
    * 表大概的样子

        | id | form |
        |----|------|
        | 0  | 济   |
        | 1  | 借   | 
        | 2 | 手   |  


* 常用字表 (common_forms)

    * 表大概的样子

        | id | form |
        |----|------|
        | 13  | 借   |

* 常用字正体字关联表 (std_common_associations)

    * 比如用户搜借，根据不用场景，我们先搜一遍常用字表，得到了常用字的id，拿着这个id，来这个关联表，可以找到它所对应的所有正字，以及为什么
    * 表大概的样子

        | standard_form_id | common_form_id | explanation  | 
        |------|---|----|
        |  0   | 13 |  因为上山下乡，济不小心就变成了借 |


* 词表 (words)

    * 表大概的样子

        | id | standard_form | common_form |
        |----|------|-----|
        | 56  | 濟手   | 借手 |



* 字发音表 (form_pronounciations)

    * 不是每个列都必须有数据的，前端有啥显示啥
    * 一个正字可以有多个发音
    * 表大概的样子

        |  standard_form_id | pinyin | wu  | canton | phonetics
        |----|---|---|-----|-----|
        | 0 |  ji | tci,213  | null |  null  |

* 词发音表 (word_pronounciations)

    * 不是每个列都必须有数据的，前端有啥显示啥
    * 一个词可以有多个发音
    * 表大概的样子

        |  word_id | pinyin | wu  | canton | phonetics
        |----|---|---|-----|-----|
        | 56 |  jiasei | ((tcia, 213),(sei, 52)) | null |  null  |
        | 56 |  jisei | ((tci, 213),(sei, 52))  | null |  null  |

* 意思表

    * 表大概的样子

        | category | mapping_id | word_or_form | meaning |
        |--------|-----|----|----|
        | verb | 1 | 字 | 用别人的，但是要还，有～有还，再借不难
        | verb | 0 | 字 | 帮助，～世救人
        | noun | 56 | 词 | 左手


* 文献表

    * 表大概的样子

        |  id | display_name | category | author  | published_at
        |----|---|---|----|----|
        | 0 |  杭州方言词典 |  词典 |  鲍士杰 | null

* 文献与词字词关联表

    * 表大概的样子

        | source_id | mapping_id | word_or_form | data |
        |--------|-----|----|----|
        | 0 | 3 | 字 | {key: value, key: value, key: value}
        | 0 | 56 | 词 | {key: value, key: value, key: value}

