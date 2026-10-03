from django.db import transaction

from db.models import Order


@transaction.atomic
def create_order(tickets: list[dict], username: str, date: str | None=None) -> Order:
    result = Order.objects.create(tickets=tickets, username=username)
    if date is not None:
        result.created_at = date
    return result
