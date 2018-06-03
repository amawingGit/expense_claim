from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

from app.models.expense_claim import ExpenseClaim
from app.models.user import User
# from app.models.expense_department import ExpenseDepartment
# from app.models.approval import Approval
