from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean, desc, func

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "public"}
    age = Column(Integer)
    city = Column(String)
    country = Column(String)
    exp_group = Column(Integer)
    gender = Column(Integer)
    id = Column(Integer, primary_key=True)
    os = Column(String)
    source = Column(String)
    

if __name__ == "__main__":
    sessios = SessionLocal()
    response = sessios.query(User.country, User.os, func.count(User.id).label('count')).filter(User.exp_group == 3).group_by(User.country, User.os).having(func.count(User.id) > 100).order_by(desc(func.count(User.id))).all()
    result = [(x.country, x.os, x.count)  for x in response]
    print(result)
