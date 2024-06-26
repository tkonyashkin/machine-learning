from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean, desc, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from table_post import Post
from table_user import User

class Feed(Base):
    __tablename__ = "feed_action"
    __table_args__ = {"schema": "public"}
    action = Column(String)
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True)
    post = relationship(Post)
    time = Column(DATETIME)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user = relationship(User)