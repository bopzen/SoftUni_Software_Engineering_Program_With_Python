"""Add Chefs Table

Revision ID: 1df2e471c846
Revises: b9049b18d1bf
Create Date: 2023-11-16 16:00:30.325716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1df2e471c846'
down_revision: Union[str, None] = 'b9049b18d1bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'chefs', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chefs', type_='unique')
    # ### end Alembic commands ###