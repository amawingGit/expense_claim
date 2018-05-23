from app.models import Base
from sqlalchemy import Column, String,  DateTime, Integer, func

 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    updated_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
 