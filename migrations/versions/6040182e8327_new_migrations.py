"""new_migrations

Revision ID: 6040182e8327
Revises: 2bd1ccb8abde
Create Date: 2024-04-26 17:44:30.727343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6040182e8327'
down_revision = '2bd1ccb8abde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quiztitle', sa.String(), nullable=True))
        batch_op.drop_index('ix_users_email')
        batch_op.create_index(batch_op.f('ix_users_quiztitle'), ['quiztitle'], unique=False)
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(), nullable=True))
        batch_op.drop_index(batch_op.f('ix_users_quiztitle'))
        batch_op.create_index('ix_users_email', ['email'], unique=1)
        batch_op.drop_column('quiztitle')

    # ### end Alembic commands ###
