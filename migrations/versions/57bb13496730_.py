"""empty message

Revision ID: 57bb13496730
Revises: 
Create Date: 2021-03-20 15:38:04.040057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57bb13496730'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('student_id')
    )
    op.create_table('test_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('elapsed_time_ms', sa.Integer(), nullable=False),
    sa.Column('platform', sa.String(length=32), nullable=True),
    sa.Column('browser', sa.String(length=32), nullable=True),
    sa.Column('browser_version', sa.String(length=8), nullable=True),
    sa.Column('language', sa.String(length=32), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_responses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_result_id', sa.Integer(), nullable=False),
    sa.Column('is_example', sa.Boolean(), nullable=False),
    sa.Column('question_num', sa.Integer(), nullable=False),
    sa.Column('response', sa.Integer(), nullable=False),
    sa.Column('correct', sa.Boolean(), nullable=False),
    sa.Column('elapsed_time_ms', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['test_result_id'], ['test_results.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_responses')
    op.drop_table('test_results')
    op.drop_table('users')
    # ### end Alembic commands ###