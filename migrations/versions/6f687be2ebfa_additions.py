"""additions

Revision ID: 6f687be2ebfa
Revises: 7b93523321f1
Create Date: 2022-04-01 14:14:10.932284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f687be2ebfa'
down_revision = '7b93523321f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_notifications_timestamp'), 'user_notifications', ['timestamp'], unique=False)
    op.create_table('post_response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('response_to_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['response_to_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_response_score'), 'post_response', ['score'], unique=False)
    op.create_index(op.f('ix_post_response_timestamp'), 'post_response', ['timestamp'], unique=False)
    op.add_column('post', sa.Column('thread', sa.String(length=127), nullable=True))
    op.create_index(op.f('ix_post_thread'), 'post', ['thread'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_thread'), table_name='post')
    op.drop_column('post', 'thread')
    op.drop_index(op.f('ix_post_response_timestamp'), table_name='post_response')
    op.drop_index(op.f('ix_post_response_score'), table_name='post_response')
    op.drop_table('post_response')
    op.drop_index(op.f('ix_user_notifications_timestamp'), table_name='user_notifications')
    op.drop_table('user_notifications')
    # ### end Alembic commands ###
