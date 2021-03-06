"""empty message

Revision ID: f0cdb47e0dff
Revises: 
Create Date: 2019-12-24 09:23:17.561217

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f0cdb47e0dff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('writers')
    op.drop_table('user')
    op.drop_table('books')
    op.drop_table('shelfing')
    op.drop_table('book_tag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_tag',
    sa.Column('book_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('tag_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('book_id', 'tag_id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('shelfing',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('tag', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('books',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('phone', mysql.VARCHAR(length=11), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('reg_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('writers',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    # ### end Alembic commands ###
