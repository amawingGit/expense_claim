from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

from app.models.user import User
from app.models.expense_claim import ExpenseClaim