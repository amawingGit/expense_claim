from sqlalchemy import Column, Integer, DateTime, ForeignKey, Index, String, Date,func
from app.models import Base
from sqlalchemy.orm import relationship


BUDGET_CATEGORIES = ['finance', 'engineering', 'channel' ]

class ExpenseClaim(Base):
    __tablename__ = 'expense_claims'
    id = Column(Integer, primary_key=True)
    vendor_name = Column(String)
    effective_date = Column(Date)
    invoice_reference = Column(String(256))
    amount = Column(Integer)
    currency_code = Column(String(8))
    budget_category = Column(String)
    comment = Column(String(1024))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    user = relationship('User')
    updated_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())

    def categories(self):
      return BUDGET_CATEGORIES
 
