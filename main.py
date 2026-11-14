from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
app=FastAPI()
class Post(BaseModel):
    title:str
    content:str
    published:bool=True #default value is true
    rating:Optional[int]=None #default it is null or int thats the use of optional

@app.get("/")
def root():
    return {"message":"Hello world"}
@app.get("/posts")
def get_posts():
    return {"Hi":"Welcome to posts"}
@app.post("/createposts")
def create_posts(post:Post): #previously it was Body but now it redirects to post class
    print(post)
    print(post.dict()) #convertion from json to dict 
    return{"data":post}
