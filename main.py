from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def root():
    return {"message":"Hello world"}
@app.get("/posts")
def get_posts():
    return {"Hi":"Welcome to posts"}