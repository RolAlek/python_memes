"""add filename field

Revision ID: 7884fb28dc30
Revises: c89a4738a9bc
Create Date: 2024-06-27 23:11:33.471106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '7884fb28dc30'
down_revision: Union[str, None] = 'c89a4738a9bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('memes', sa.Column('file_name', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('memes', 'file_name')
