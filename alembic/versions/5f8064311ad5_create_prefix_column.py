"""create prefix column

Revision ID: 5f8064311ad5
Revises: 262d3b35c974
Create Date: 2023-07-27 05:32:56.976068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f8064311ad5'
down_revision = '262d3b35c974'   
branch_labels = None
depends_on = None


def upgrade() :
    op.add_column('route', sa.Column('prefix', sa.Integer(), nullable=True))


def downgrade() -> None:
    pass
