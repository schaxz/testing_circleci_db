"""empty message

Revision ID: 558d2d8d5eda
Revises: 
Create Date: 2020-01-30 20:12:57.374631

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '558d2d8d5eda'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bills',
    sa.Column('id', sa.String(length=128), nullable=False),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.Column('updated_ts', sa.DateTime(), nullable=True),
    sa.Column('owner_id', sa.String(length=128), nullable=False),
    sa.Column('vendor', sa.Text(), nullable=False),
    sa.Column('bill_date', sa.Date(), nullable=False),
    sa.Column('due_date', sa.Date(), nullable=False),
    sa.Column('amount_due', sa.Float(precision=2, asdecimal=True), nullable=False),
    sa.Column('categories', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('paymentStatus', postgresql.ENUM('paid', 'due', 'past_due', 'no_payment_required', name='payment_code'), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bills')
    # ### end Alembic commands ###