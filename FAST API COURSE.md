# FAST API COURSE

- has ability to do asynchronous programming which is absent in django  and flask 

- inbuilt swagger UI
- another inbuild docs -  ReDoc 
- uses more moder python3.6 with type using pydantic
- based on open standards  - JSON Schema, Open API
- fastapi is built over starlette supports (websocket, graphQL, In-progress background tasks, startup and shutdown events)
- supports sql, no-sql and graphQL

---

## Concepts

- Install and Setup

### Basics Concepts

- Path Parameters
- API Docs - swagger/redocs
- Query parameters
- Request body

### Intermediate Concepts

- Debugging FastAPI
- Pydantic schemas
- SqlAlchemy and database connection
- Models and table

### Database Tasks

-  Strore blog to database
- Get blogs from database
- Delete
- Update

### Responses

- Handling Exceptions
- Return response
- Define response model

### User and Password

- Create user

- Hash user password

- Show single user

- Define  docs tags

### Relationship

- Define user to blog relationship

- Define blog to user relationship

### Refactor for Bigger Application

- API Router

- API Router with parameters

### Authentication using JWT

- Create Login route

- Login and verify password

- Return JWT access token

- Routes behind authentication

### Deploy FastAPI

- Using Det.sh website to deploy

---

## Installation and Setup

1. Create Virtual env in python (.\Documents\FAST_API)

   - python -m venv fastapi_env

2.  Activate virtual env fastapi_env

   - fastapi_env\Scripts\activate.bat

3. Install fastapi packages

   - pip3 install fastapi

   - pip3 install uvicorn



#### Basic API code 

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'hello fast api coder'
```

Command to run api :    **uvicorn main:app --reload**

command to check uvicorn version: **uvicorn --version**

```python
# simple fast json api 
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'home':'Vasi Krish'}}
```

