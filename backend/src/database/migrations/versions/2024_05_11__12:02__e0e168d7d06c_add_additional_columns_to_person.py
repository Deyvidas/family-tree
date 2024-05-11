"""add additional columns to person

Revision ID: e0e168d7d06c
Revises: 125ecee4b828
Create Date: 2024-05-11 12:02:29.656433+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "e0e168d7d06c"
down_revision: Union[str, None] = "125ecee4b828"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("person", sa.Column("name", sa.String(), nullable=False))
    op.add_column("person", sa.Column("surname", sa.String(), nullable=False))
    op.add_column(
        "person", sa.Column("patronymic", sa.String(), nullable=False)
    )
    op.add_column(
        "person",
        sa.Column(
            "gender",
            sa.Enum("male", "female", name="enumgender"),
            nullable=False,
        ),
    )
    op.add_column("person", sa.Column("birth_date", sa.Date(), nullable=False))
    op.drop_column("person", "last_name")
    op.drop_column("person", "first_name")


def downgrade() -> None:
    op.add_column(
        "person",
        sa.Column(
            "first_name", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "person",
        sa.Column(
            "last_name", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )
    op.drop_column("person", "birth_date")
    op.drop_column("person", "gender")
    op.drop_column("person", "patronymic")
    op.drop_column("person", "surname")
    op.drop_column("person", "name")
