from .api.notifications import (
    create_destination,
    create_subscription,
    delete_destination,
    delete_subscription_by_id,
    get_destination,
    get_destinations,
    get_subscription,
    get_subscription_by_id,
)
from .client import Client

__all__ = (
    "Client",
    "get_subscription",
    "create_subscription",
    "get_subscription_by_id",
    "delete_subscription_by_id",
    "get_destinations",
    "create_destination",
    "get_destination",
    "delete_destination",
)
