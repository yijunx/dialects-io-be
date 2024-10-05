# dialects-io-be

this is the backend!!

### functional requirements

* 搜索（包括字、詞）（我們說的詞包括詞彙、俗語等）
    * 用户输入拼音搜寻
        * 吴语拼音（主要拼音搜索功能，附教程）
        * 国际音标（也可以沒有這個功能）
    * 用户输入汉字搜索（词汇包括正字、俗字）
    * 用户输入释义搜索（今后可以模糊搜索，例子：“一塌刮子，釋義：總共”，如果搜索“全部”也可以搜到。該功能成本略高，需要向量数据库，甚至chatbot）

* 显示
    * 字，按照正体字（繁體字）显示 
        * 簡體写法
        * 標準吳拼（按照當代杭州話發音規定的標準音，标准音可能有多个，所以我們分開儲存，但顯示的時候同時顯示）
        * 各類发音（按照出處+時間排序，並且可以點擊進入到出處中該字的位置）
        * 组词，可以点击词进入词的页面
    * 词，按照正体（繁體字）显示
        * 標準簡體写法
        * 各類白字、俗字、疑似正字（主要是方便搜索之用）
        * 標準吳拼（按照當代杭州話發音規定的標準音）
        * 標準釋義（按照出處整合而成，若無出處，則需自己編寫）
        * 各類发音和釋義（按照出處+時間排序，並且可以點擊進入到出處中該詞的位置）
        * 造句（用戶可以上傳自己的造句以及錄音，這樣提高了交互性，可增加數據庫豐富度）
        * 注：用户可以点击每个字进入字的页面

* 信息录入
    * 必须登录，后端核实为contributor

### database design

* 字表 (standard_chars)

    * 意思和发音会被存入另外的表
    * 表大概的样子

        | id | form | wupin | etc. |
        |----|------|------|------|
        | 0  | 濟   | tci 陰去 | ... |
        | 1  | 借   | tci 陰去 | ... |
        | 2  | 借   | tcia 陰去 | ... |
        | 3 | 手   |  sei 上 | ... |


* 标准词表 (standard_words)

    * 表大概的样子

        | id | form | interpretation |wupin |  etc. |
        |----|------|------|------|------|
        | 56  | 濟手 | 左手（名词） | tci sei  | ... |
        | 57  | 濟手 | 左手（名词） | tcia sei | ... |

* 常用词表 (common_words)

    * 表大概的样子

        | id | form | reference |interpretation | etc. |
        |----|------|------|------|------|
        | 22  | 濟手 | 某書第XXX頁 | ... |... |
        | 23  | 借手 | 某書第XXX頁 | ... |... |
        | 24  | 借手 | 某書第XXX頁 | ... |... |
        | 25  | 假手 | 某書第XXX頁 | ... |... |

* 標準詞-常用詞关联表 (std_common_word_associations)

    * 比如用户搜“借手”，我们先搜一遍常用詞表獲得id，然後利用標準詞-常用詞关联表找到和標準詞。
    * 表大概的样子

        | standard_id | common_id |
        |------|---|
        |  56   | 23 |
        |  56   | 24 |
        |  ...  | ... |


———————————————— 暫時改到這裡 ————————————————

 
* 字发音表 (form_pronounciations)

    * 不是每个列都必须有数据的，前端有啥显示啥
    * 一个正字可以有多个发音
    * 表大概的样子

        |  standard_id | pinyin | wu  | canton | phonetics
        |----|---|---|-----|-----|
        | 0 |  ji | tci,213  | null |  null  |

* 词发音表 (word_pronounciations)

    * 不是每个列都必须有数据的，前端有啥显示啥
    * 一个词可以有多个发音
    * 表大概的样子

        |  standard_id | pinyin | wu  | canton | phonetics
        |----|---|---|-----|-----|
        | 56 |  jiasei | ((tcia, 213),(sei, 52)) | null |  null  |
        | 56 |  jisei | ((tci, 213),(sei, 52))  | null |  null  |

* 意思表

    * 表大概的样子

        | category | standard_id | word_or_char | meaning |
        |--------|-----|----|----|
        | verb | 1 | char | 用别人的，但是要还，有～有还，再借不难
        | verb | 0 | char | 帮助，～世救人
        | noun | 56 | word | 左手


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

