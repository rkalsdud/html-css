"""initial

Revision ID: 4794f29f40d4
Revises: 
Create Date: 2025-02-16 17:16:13.948724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4794f29f40d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=64), nullable=True))
        batch_op.create_index('ix_users_email', ['email'], unique=1)

    # ### end Alembic commands ###
