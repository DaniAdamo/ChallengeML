from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddaea09c62fa'
down_revision = '935ff2a7d649'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    users=op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('rol', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    listuser = [
        {
            "username": "admin",
            "password": "$2b$12$MTzBx7m6dkpxK06t3itHz.9RTbL6FCJFnatgDIXUXsOhv2Ipt/Nte",
            "rol": 1
        },
        {
            "username": "Nico",
            "password": "$2b$12$koBoshAnLq0cno7GLY378e0vWau5ljxkg.DhvJz4aIBIUE339pqQC",
            "rol": 2
        },
        {
            "username": "Silvia",
            "password": "$2b$12$kBBuEGFqPntGrsuEVg48WeF7EQL4evx2T/5l1zFzG1MSXu5lgitE6",
            "rol": 3
        }
    ]
    op.bulk_insert(users, listuser)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
