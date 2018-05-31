from sqlalchemy import Column, Integer, DateTime, ForeignKey, Index, String, Date,func
from app.models import Base
from sqlalchemy.orm import relationship

STATUS = ['approved', 'declined', 'open', 'closed', 'rejected']

class Approval(Base):
    __tablename__ = 'approvals'
    id = Column(Integer, primary_key=True)
    status = Column(String)          
    expense_claim_id = Column(Integer, ForeignKey('expense_claims.id'), nullable=False, index=True)
    expense_claim = relationship('ExpenseClaim')
    #level_1_user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    level_1_user = relationship('User')
    #level_2_user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    level_2_user = relationship('User')
    amount = Column(Integer)
    comment = Column(String)
    updated_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
