from fastapi import FastAPI,Response,status,HTTPException
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

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            print("Found",id)
            return p
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i #gets the index od the id
@app.get("/")
def root():
    return {"message":"Hello world"}
@app.get("/posts")
def get_posts():
    return {"Hi":"Welcome to posts"}
@app.post("/createposts",status_code=status.HTTP_201_CREATED) #just status that it is cerated 
def create_posts(post:Post): #previously it was Body but now it redirects to post class
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000)
    my_posts.append(post_dict)
    print(post_dict)
    print(my_posts)
    return{"data":post_dict}
@app.get("/posts/{id}")#the found id is sent here
def get_post(id: int): #id is string as it is in url so convert to int 
    post=find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found"
        )
    
    return {"post_detail":post}
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id) #gets the index
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist"
        )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT) #no content masn status is deleted 


@app.put("/posts/{id}") #lets take the id=1 of the haraadcoded value
def update_post(id: int, post: Post): #post is the data i enter 
    index = find_index_post(id)#gets the index ..index=0
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist"
        )
    post_dict = post.dict() #it has the title,content, published, rating because the id to update is entered in the text box only 
    post_dict['id'] = id # here only the id which i entered in text box is added the post_dict hte new values i entered 
    my_posts[index] = post_dict #replace mypost[0] with this new post_dict
    return {"data": post_dict}
#in the fast api platform if u type http://127.0.0.1:8000/docs here if u type just title and conetn it will automatically assign id  