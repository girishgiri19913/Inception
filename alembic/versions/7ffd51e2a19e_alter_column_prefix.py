"""alter column prefix

Revision ID: 7ffd51e2a19e
Revises: 5f8064311ad5
Create Date: 2023-08-07 06:08:18.572619

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = '7ffd51e2a19e'
down_revision = '5f8064311ad5'   
branch_labels = None
depends_on = None


def upgrade() :
    op.add_column('route', sa.Column('new_prefix', sa.String(), nullable=True))

    connection = op.get_bind()

    # Use SQLAlchemy's text() construct to execute the SQL statement
    connection.execute(text("UPDATE route SET new_prefix = CAST(prefix AS VARCHAR)"))

    op.drop_column('route', 'prefix')
    op.alter_column('route', 'new_prefix', new_column_name='prefix')
 

def downgrade() -> None:
    pass
