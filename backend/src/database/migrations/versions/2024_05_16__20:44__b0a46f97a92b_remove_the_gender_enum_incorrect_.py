"""remove the gender enum incorrect ordering

Revision ID: b0a46f97a92b
Revises: ea96b311b71b
Create Date: 2024-05-16 20:44:19.873263+00:00

"""

from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


revision: str = "b0a46f97a92b"
down_revision: Union[str, None] = "ea96b311b71b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "person",
        "gender",
        existing_type=postgresql.ENUM("male", "female", name="enumgender"),
        type_=sa.String(),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "person",
        "gender",
        existing_type=sa.String(),
        type_=postgresql.ENUM("male", "female", name="enumgender"),
        existing_nullable=False,
    )
