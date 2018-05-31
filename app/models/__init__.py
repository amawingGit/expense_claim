from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Test(Base):
    id = Column(Integer, primary_key = True)
    name = Column(String(64))

from app.models.user import User
# from app.models.expense_claim import ExpenseClaim
# from app.models.expense_department import ExpenseDepartment
# from app.models.approval import Approval
