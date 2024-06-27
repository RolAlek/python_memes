"""first migration

Revision ID: c89a4738a9bc
Revises: 
Create Date: 2024-06-27 02:14:44.528182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'c89a4738a9bc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('memes',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('added', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('memes')
