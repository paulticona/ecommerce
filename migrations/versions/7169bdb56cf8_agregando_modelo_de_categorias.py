"""Agregando modelo de categorias

Revision ID: 7169bdb56cf8
Revises: c6c92392dc0e
Create Date: 2022-09-21 13:42:53.788539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7169bdb56cf8'
down_revision = 'c6c92392dc0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###