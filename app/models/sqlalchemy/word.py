from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, Index, BIGINT, VARCHAR, Integer, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.sqlalchemy.base import Base, AdminRecord




class StandardCharRecord(AdminRecord):
    __tablename__ = "standard_char"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)

    # 标准字形
    content: Mapped[str] = mapped_column(VARCHAR(1), nullable=False, index=True)

    description: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)

class StandardWordORM(AdminRecord):
    __tablename__ = "standard_word"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)


class CharWordAssociationRecord(AdminRecord):
    __tablename__ = "char_word_association"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    char_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    word_id: Mapped[str] = mapped_column(BIGINT, nullable=False, index=True)
    char_position: Mapped[int] = mapped_column(Integer, nullable=False)


class CharRecord(AdminRecord):
    __tablename__ = "daily_char"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    standard_char_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    content: Mapped[str] = mapped_column(VARCHAR(1), nullable=False, index=True)


class CharSourceAssociationRecord(AdminRecord):
    __tablename__ = "char_source_association"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    char_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    source_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)

    page_number: Mapped[int] = mapped_column(Integer, nullable=True)

    # consonant for 同 is 定 in 广韵
    consonant: Mapped[str] = mapped_column(VARCHAR(10), nullable=True)

    # vovel for 同 is 東 in 广韵
    vowel: Mapped[str] = mapped_column(VARCHAR(10), nullable=True)

    # tone for 同 is 平 in 广韵
    tone: Mapped[str] = mapped_column(VARCHAR(10), nullable=True)

    # 等是用来分类韵母的发音位置或口腔开合度的概念
    # 一等：舌位最靠后，发音时口腔最张开。
    # 二等：舌位略向前，发音时口腔张开度稍小。
    # 三等：舌位向前，发音时口腔较为闭合。
    # 四等：舌位最靠前，发音时口腔最闭合。
    # in fact they describe i, u, v in pinyin
    # deng for 同 is 一 in 广韵
    deng: Mapped[str] = mapped_column(VARCHAR(10), nullable=True)

    # 在学术文献中，通常直接采用音译 fanqie。这种翻译方式保留了反切的原有概念，特别是在音韵学研究中很常见。
    # 🍅 for 同 is 徒紅 in 广韵
    fanqie: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    # rhyme catefory for 同 is canton in 广韵 （废话）
    rhyme_category: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)

    phonetic_vowel: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    phonetic_consonant: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)
    phonetic_tone: Mapped[str] = mapped_column(VARCHAR(20), nullable=True)

    meaning: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    pronouciation_storage_uri: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)

class WordRecord(AdminRecord):
    __tablename__ = "daily_word"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    standard_word_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    content: Mapped[str] = mapped_column(VARCHAR(10), nullable=False, index=True)

    
class WordSourceAssociationRecord(AdminRecord):
    __tablename__ = "word_source_association"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    word_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    source_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)

    page_number: Mapped[int] = mapped_column(Integer, nullable=True)

    
    pronouciation_storage_uri: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    notes: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)

    tags: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    meaning: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)


class SentenceRecord(AdminRecord):
    __tablename__ = "daily_sentence"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    content: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, index=True)
    meaning: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)


class SentenceCharAssociationRecord(AdminRecord):
    __tablename__ = "sentence_char_association"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    sentence_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    char_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    char_position: Mapped[int] = mapped_column(Integer, nullable=False)
  






# class PronounciationORM(AdminRecord):
#     __tablename__ = "pronounciations"
#     id: Mapped[str] = mapped_column(String, primary_key=True)
#     charactor_id: Mapped[str] = mapped_column(String, nullable=False)

#     # 標準音，普通話拼音
#     pinyin: Mapped[str] = mapped_column(String, nullable=True, index=True)
#     # 標準音，吳語拼音
#     wu: Mapped[str] = mapped_column(String, nullable=True)
#     # 標準音，廣韻
#     canton: Mapped[str] = mapped_column(String, nullable=True)
#     # 標準音，國際音標
#     phonetic: Mapped[str] = mapped_column(String, nullable=True)

#     # 描述
#     description: Mapped[str] = mapped_column(String, nullable=True)








