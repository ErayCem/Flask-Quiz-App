"""Initial migration

Revision ID: 7a49bc06778d
Revises: 
Create Date: 2025-05-02 21:13:57.747629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a49bc06778d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=500), nullable=False),
    sa.Column('option_a', sa.String(length=200), nullable=False),
    sa.Column('option_b', sa.String(length=200), nullable=False),
    sa.Column('option_c', sa.String(length=200), nullable=False),
    sa.Column('option_d', sa.String(length=200), nullable=False),
    sa.Column('correct_option', sa.String(length=1), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('score',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('score')
    op.drop_table('user')
    op.drop_table('question')
    # ### end Alembic commands ###
