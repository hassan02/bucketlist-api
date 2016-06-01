"""empty message

Revision ID: a20149dc4aab
Revises: 162c0569049c
Create Date: 2016-05-21 16:45:07.779000

"""

# revision identifiers, used by Alembic.
revision = 'a20149dc4aab'
down_revision = '162c0569049c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('bucket_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('bucket_list_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('bucketlist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bucketlist_id'], ['bucket_list_model.id'], ),
    sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('users')
    op.drop_table('bucket_list')
    op.drop_table('bucket_list_item')
