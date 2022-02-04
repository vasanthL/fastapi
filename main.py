# initialize libs
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'home':'Vasi'}}

@app.get('/about')
def about():
    return {'data':'about page'}