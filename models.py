from typing import Optional

from sqlmodel import Field, SQLModel

class JokeBase(SQLModel):
    joke: str = Field(min_length=1, max_length=500)

class Joke(JokeBase, table=True):
    number:Optional[int] = Field(default=None, primary_key=True)

class JokeCreate(JokeBase):
    pass

class JokeResponse(JokeBase):
    number: int

class JokeUpdate(JokeBase):
    number: int