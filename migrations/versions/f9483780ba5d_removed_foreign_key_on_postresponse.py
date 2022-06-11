"""removed foreign key on PostResponse

Revision ID: f9483780ba5d
Revises: 14e10f55f257
Create Date: 2022-06-10 23:38:25.488153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9483780ba5d'
down_revision = '14e10f55f257'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_response', sa.Column('response_to_user_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post_response', 'response_to_user_id')
    # ### end Alembic commands ###