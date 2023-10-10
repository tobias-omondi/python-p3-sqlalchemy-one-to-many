"""Add platform column to Game

Revision ID: 18805b306342
Revises: 675d97e1c69f
Create Date: 2023-10-10 13:46:23.808539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18805b306342'
down_revision = '675d97e1c69f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('platform', sa.String(), nullable=True))
        batch_op.drop_column('plantform')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('plantform', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('platform')

    # ### end Alembic commands ###
