from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from random import randrange
app=FastAPI()
class Post(BaseModel):
    title:str
    content:str
    published:bool=True #default value is true
    rating:Optional[int]=None #default it is null or int thats the use of optional
my_posts=[
    {"title":"title of post 1","content":"content of post 1","id":1},
    {"title":"favorite foods","content":"I like pizza","id":2}
] #in terminal we gave--reload since its in ram it reloads everytime and comes back to this hardcoded 2 values 

@app.get("/")
def root():
    return {"message":"Hello world"}
@app.get("/posts")
def get_posts():
    return {"Hi":"Welcome to posts"}
@app.post("/createposts")
def create_posts(post:Post): #previously it was Body but now it redirects to post class
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000)
    my_posts.append(post_dict)
    print(post_dict)
    print(my_posts)
    return{"data":post_dict}
#in the fast api platform if u type http://127.0.0.1:8000/docs here if u type just title and conetn it will automatically assign id  