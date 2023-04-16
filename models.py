from typing import Optional

from sqlmodel import Field, SQLModel

class JokeBase(SQLModel):
    joke:str

class Joke(JokeBase, table=True):
    number:Optional[int] = Field(default=None, primary_key=True)

class JokeCreate(JokeBase):
    pass

class JokeResponse(JokeBase):
    number: int
    joke:str

class JokeUpdate(JokeBase):
    pass
