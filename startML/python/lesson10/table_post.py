from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean, desc

class Post(Base):
    __tablename__ = "post"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)
    
    
    
if __name__ == "__main__":
    sessios = SessionLocal()
    response = sessios.query(Post).filter(Post.topic == 'business').order_by(desc(Post.id)).limit(10).all()
    result = [x.id for x in response]
    print(result)