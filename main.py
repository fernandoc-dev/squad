from fastapi import FastAPI
import requests

app = FastAPI(title='The title',
              description='The description',
              version=1)

@app.get('/')
async def index():  # For asynchronous answer
    return 'Hello world'