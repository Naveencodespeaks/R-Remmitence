"""ttest

Revision ID: e123f197a9e5
Revises: 
Create Date: 2024-08-11 14:17:05.102287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e123f197a9e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=61), nullable=True),
    sa.Column('password', sa.Text(), nullable=True),
    sa.Column('login_token', sa.Text(), nullable=True),
    sa.Column('token', sa.Text(), nullable=True),
    sa.Column('email', sa.String(length=161), nullable=True),
    sa.Column('mobile_no', sa.String(length=13), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('md_user_roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_md_user_roles_name'), 'md_user_roles', ['name'], unique=False)
    op.create_table('md_user_status',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=61), nullable=True),
    sa.Column('password', sa.String(length=10), nullable=True),
    sa.Column('login_token', sa.Text(), nullable=True),
    sa.Column('email', sa.String(length=161), nullable=False),
    sa.Column('mobile_no', sa.String(length=13), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('kyc_status', sa.Enum('PENDING', 'COMPLETED', name='kycstatus'), nullable=False, comment='The status of the user (e.g., pending==0, completed==1)'),
    sa.Column('login_fail_count', sa.Integer(), nullable=True),
    sa.Column('login_attempt_date', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['md_user_roles.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['md_user_status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('md_user_status')
    op.drop_index(op.f('ix_md_user_roles_name'), table_name='md_user_roles')
    op.drop_table('md_user_roles')
    op.drop_table('admin')
    # ### end Alembic commands ###
