"""Renaming students to scholars

Revision ID: b4270ccdd95d
Revises: 791279dd0760
Create Date: 2025-02-28 15:50:57.320910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4270ccdd95d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
