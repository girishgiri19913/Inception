"""add track project id

Revision ID: 262d3b35c974
Revises: dc81a8aac431
Create Date: 2023-07-19 07:02:54.401358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '262d3b35c974'
down_revision = 'dc81a8aac431'
branch_labels = None
depends_on = None


def upgrade() :
    op.add_column('track', sa.Column('project_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_track_project_id_projects', 'track', 'projects', ['project_id'], ['id'])


def downgrade() -> None:
    pass
