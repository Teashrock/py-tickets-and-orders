from datetime import datetime
from db.models import Order, Ticket


from django.db import transaction
from django.contrib.auth import get_user_model
User = get_user_model()


@transaction.atomic
def create_order(
    tickets: list[dict],
    username: str,
    date: str | None = None
) -> Order:
    user = User.objects.get(username=username)

    order_data = {"user": user}
    if date:
        order_data["created_at"] = datetime.strptime(date, "%Y-%m-%d %H:%M")

    order = Order.objects.create(**order_data)

    for ticket_data in tickets:
        Ticket.objects.create(
            order=order,
            movie_session_id=ticket_data["movie_session"],
            row=ticket_data["row"],
            seat=ticket_data["seat"]
        )

    return order


def get_orders(username: str | None = None) -> list[Order]:
    if username:
        return Order.objects.filter(user__username=username)
    return Order.objects.all()
