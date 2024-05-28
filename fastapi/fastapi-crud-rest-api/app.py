from fastapi import FastAPI , HTTPException , status
from pydantic import BaseModel #Modelo inicial, como van a lucir nuestros datos
from typing import Text, Optional
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from uuid import uuid4 as uuid

app = FastAPI()

posts = []

# Post Model
class Post(BaseModel):
    id: Optional[str] = None
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime] = None
    published: bool = False

@app.get('/')
def read_root():
    return { "welcome":"welcome to my REST API" }

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post : Post):    
    post.id = str(uuid())
    post_dict = jsonable_encoder(post)
    posts.append(post_dict)
    return posts[-1]#el ultimo

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    print(post_id)
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post Not found")

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    #enumarate nos da la publicacion y el indice
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post has been deleted successfully"}
    raise HTTPException(status_code=404, detail="Post Not found")

@app.put('/posts/{post_id}')
def update_post(post_id: str,updatedPost: Post):
    for index,post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"] = updatedPost.title
            posts[index]["author"] = updatedPost.author
            posts[index]["content"] = updatedPost.content
            return {"message": "Post has been updated successfully"}
    raise HTTPException(status_code=404, detail="Post Not found")