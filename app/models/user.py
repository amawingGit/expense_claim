from app.models import Base
from sqlalchemy import Column, String,  DateTime, Integer, func


ROLES = ['user', 'level-1', 'level-2', 'admin']
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    updated_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
 
    def __repr__(self):
        return "<User(name='%s', role='%s')>" % (self.name, self.role)
