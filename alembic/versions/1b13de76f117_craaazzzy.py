"""craaazzzy

Revision ID: 1b13de76f117
Revises: 
Create Date: 2018-06-01 15:34:50.275693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b13de76f117'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('expense_approvers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department', sa.String(), nullable=True),
    sa.Column('approver_role', sa.String(), nullable=True),
    sa.Column('approver_id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['approver_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_expense_approvers_approver_id'), 'expense_approvers', ['approver_id'], unique=False)
    op.create_table('expense_claims',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vendor_name', sa.String(), nullable=True),
    sa.Column('effective_date', sa.Date(), nullable=True),
    sa.Column('invoice_reference', sa.String(length=256), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('currency_code', sa.String(length=8), nullable=True),
    sa.Column('budget_category', sa.String(), nullable=True),
    sa.Column('comment', sa.String(length=1024), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_expense_claims_user_id'), 'expense_claims', ['user_id'], unique=False)
    op.create_table('approvals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('expense_claim_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['expense_claim_id'], ['expense_claims.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_approvals_expense_claim_id'), 'approvals', ['expense_claim_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_approvals_expense_claim_id'), table_name='approvals')
    op.drop_table('approvals')
    op.drop_index(op.f('ix_expense_claims_user_id'), table_name='expense_claims')
    op.drop_table('expense_claims')
    op.drop_index(op.f('ix_expense_approvers_approver_id'), table_name='expense_approvers')
    op.drop_table('expense_approvers')
    op.drop_table('users')
    # ### end Alembic commands ###
