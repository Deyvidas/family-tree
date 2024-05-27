from random import choice
from uuid import uuid4

from faker import Faker

from src.common.schema.fields import TZ_UTC
from src.interest.schema import Schema


fake = Faker(['ru_RU'])


def generate_interest() -> Schema:
    is_new = choice([True, False])
    created_at = fake.date_time_this_month(tzinfo=TZ_UTC)

    match is_new:
        case True:
            updated_at = created_at
        case False:
            updated_at = fake.date_time_between(
                start_date=created_at,
                tzinfo=TZ_UTC,
            )

    return Schema(
        id=uuid4(),
        created_at=created_at,
        updated_at=updated_at,
        name=fake.text(20),
        description=fake.text(80),
    )


def generate_interests(amount: int) -> list[Schema]:
    return [generate_interest() for _ in range(amount)]
