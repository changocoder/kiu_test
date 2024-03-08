from enum import Enum


class StatusEnum(Enum):
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELLED = 'Cancelled'
    PENDING = 'Pending'
