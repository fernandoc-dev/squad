from fastapi import FastAPI, HTTPException

from libraries.show_joke import Show_Joke
import random

from libraries.math import Math

from sqlmodel import Session
from db import engine

from models import JokeCreate,JokeResponse,JokeUpdate,Joke




app = FastAPI(title='SquadMakers',
              description='API that can make you laugh using jokes from api.chucknorris.io and icanhazdadjoke.com/api',
              version=0.1)


@app.get('/jokes')
async def jokes():
    jokes=Show_Joke()
    luck=random.randrange(1, 3, 1)
    if luck==1:
        return jokes.chuck()
    if luck==2:
        return jokes.dad()

@app.get('/jokes/{source}')
async def jokes_source(source:str):
    jokes=Show_Joke()
    if source.lower()=='chuck':
        return jokes.chuck()
    elif source.lower()=='dad':  
        return jokes.dad()
    else:
        raise HTTPException(
            status_code=422,
            detail="The source only can be Chuck or Dad"
            )
    
@app.post('/jokes',response_model=JokeResponse)
async def insert_joke(joke:JokeCreate):
    with Session(engine) as session:
        joke = Joke.from_orm(joke)
        session.add(joke)
        session.commit()
        session.refresh(joke)
        return joke

@app.patch('/jokes/{number}',response_model=JokeResponse)
async def update_joke(number:int,joke_data:JokeUpdate):
    with Session(engine) as session:
        joke = session.get(Joke, number)
        if not joke:
            raise HTTPException(status_code=404, detail="Joke not found")
        joke_data = joke_data.dict(exclude_unset=True)
        for key, value in joke_data.items():
            setattr(joke, key, value)
        session.add(joke)
        session.commit()
        session.refresh(joke)
        return joke

@app.delete('/jokes/{number}')
async def delete_joke(number):
    with Session(engine) as session:
        joke = session.get(Joke, number)
        if not joke:
            raise HTTPException(status_code=404, detail="Joke not found")
        session.delete(joke)
        session.commit()
        return {"ok": True}
    
@app.get('/lcm/{numbers}')
async def least_common_multiple(numbers):
    lcm=Math()
    return lcm.lcm([4,6,8])

@app.get('/addition/{number}')
async def addition(number:int):
    return number+1