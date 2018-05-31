from sqlalchemy import Column, Integer, DateTime, ForeignKey, Index, String, Date,func
from app.models import Base
from sqlalchemy.orm import relationship


class ExpenseDepartment(Base):
    __tablename__ = 'expense_approvers'
    id = Column(Integer, primary_key=True)
    department = Column(String)
    approver_role = Column(String)
    approver_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    approver = relationship('User')    
    updated_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
