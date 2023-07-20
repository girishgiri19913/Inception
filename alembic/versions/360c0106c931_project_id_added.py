"""project id added

Revision ID: 360c0106c931
Revises: d77b736c01b3
Create Date: 2023-07-19 03:13:03.850926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '360c0106c931'
down_revision = 'd77b736c01b3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('signal', sa.Column('project_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_signal_project_id_projects', 'signal', 'projects', ['project_id'], ['id'])


def downgrade() -> None:
    pass
