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

* 标准字表 (standard_characters)

    * 意思和发音会被存入另外的表
    * 表大概的样子

        | id | form | common_character_id | description  |
        |----|------|------|------|
        | 0  | 济   | 13  |  一些描述   |


* 常用字表

    * 比如用户输入一个常用字，后端先从此表获得id，在用这个id去标准字表找标准字
    * 表大概的样子

        | id | form | description  |
        |----|------|------|
        | 13  | 借   | 因为xx原因，  |

* 标准词表
* 常用词表
* 字发音表
* 意思表
* 文献表
* 文献与词关联表
* 文献与字关联表
