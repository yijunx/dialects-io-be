from pydantic import BaseModel




class Character(BaseModel):
    """字"""


class Word(BaseModel):
    """词"""


    characters: list[Character]



class Source(BaseModel):
    """出处"""


 