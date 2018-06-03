#from app.classes.databse_helper import
from sqlalchemy import func
from app.environment import db
from app.models.user import User
from app.models.expense_claim import ExpenseClaim

def load_seeds():
    session = db.Session()
    user = User(name='bob', role='user')
    session.add(user)

    claim = ExpenseClaim(user=user,
      vendor_name='Computer Shop',
      effective_date=func.now(),
      invoice_reference='xxxaaabbb123',
      amount=42000,
      currency_code='USD',
      budget_category='engineering',
      comment='buying laptop'
    )
    session.add(claim)
    session.commit()