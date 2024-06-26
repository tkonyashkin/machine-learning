from sqlalchemy import desc
from sqlalchemy import func
from fastapi import FastAPI, Depends, HTTPException
from schema import UserGet, PostGet, FeedGet
from database import SessionLocal
from table_user import User
from table_post import Post
from table_feed import Feed
from typing import List

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get('/user/{id}', response_model=UserGet)
def get_user(id: int, db=Depends(get_db)) -> UserGet:
    user = db.query(User).filter(User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get('/post/{id}', response_model=PostGet)
def get_post(id: int, db=Depends(get_db)) -> PostGet:
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@app.get('/user/{id}/feed', response_model=List[FeedGet])
def get_user(id: int, limit: int = 10, db=Depends(get_db)) -> List[FeedGet]:
    feed = db.query(Feed).filter(Feed.user_id == id).order_by(
        desc(Feed.time)).limit(limit).all()
    return feed


@app.get('/post/{id}/feed', response_model=List[FeedGet])
def get_post(id: int, limit: int = 10, db=Depends(get_db)) -> List[FeedGet]:
    feed = db.query(Feed).filter(Feed.post_id == id).order_by(
        desc(Feed.time)).limit(limit).all()
    return feed


@app.get('/post/recommendations/', response_model=List[PostGet])
def get_recommendations(id: int, limit: int = 10, db=Depends(get_db)) -> List[PostGet]:
    subquery = db.query(Feed.post_id, func.count(Feed.action).label('likes')).filter(
        Feed.action == 'like').group_by(Feed.post_id).order_by(desc('likes')).limit(limit).subquery()
    recommendations = db.query(Post).select_from(subquery).join(
        Post, Post.id == subquery.c.post_id
    ).all()
    return recommendations
