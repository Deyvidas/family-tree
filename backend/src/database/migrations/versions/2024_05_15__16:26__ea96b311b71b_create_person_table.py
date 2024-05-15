"""create person table

Revision ID: ea96b311b71b
Revises: 
Create Date: 2024-05-15 16:26:08.073806+00:00

"""

from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "ea96b311b71b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "person",
        sa.Column(
            "name",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "surname",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "patronymic",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "gender",
            sa.Enum("male", "female", name="enumgender"),
            nullable=False,
        ),
        sa.Column(
            "birth_date",
            sa.Date(),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
        ),
    )


def downgrade() -> None:
    op.drop_table("person")
