"""alter column xSignal

Revision ID: 9a6452d8d398
Revises: 7ffd51e2a19e
Create Date: 2023-08-08 06:15:09.387011

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = '9a6452d8d398'
down_revision = '7ffd51e2a19e'   
branch_labels = None
depends_on = None


def upgrade() :
    op.add_column('route', sa.Column('new_x_signal', sa.String(), nullable=True))

    connection = op.get_bind()

    # Use SQLAlchemy's text() construct to execute the SQL statement
    connection.execute(text("UPDATE route SET new_x_signal = CAST(x_signal AS VARCHAR)"))

    op.drop_column('route', 'x_signal')
    op.alter_column('route', 'new_x_signal', new_column_name='x_signal')


def downgrade() -> None:
    pass
