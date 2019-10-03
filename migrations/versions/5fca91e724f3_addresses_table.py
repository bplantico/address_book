"""addresses table

Revision ID: 5fca91e724f3
Revises: 
Create Date: 2019-10-03 14:25:28.902577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fca91e724f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=60), nullable=True),
    sa.Column('state', sa.String(length=60), nullable=True),
    sa.Column('zip', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_address_timestamp'), 'address', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_address_timestamp'), table_name='address')
    op.drop_table('address')
    # ### end Alembic commands ###
