"""new4_migration

Revision ID: c87812bed44c
Revises: ee2143fa0401
Create Date: 2024-04-30 10:14:44.885316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c87812bed44c'
down_revision = 'ee2143fa0401'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uploadfile', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('uploadfile')

    # ### end Alembic commands ###