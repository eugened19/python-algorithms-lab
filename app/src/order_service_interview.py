from dataclasses import dataclass
from enum import Enum

from psycopg_pool import AsyncConnectionPool


class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    FAILED = "FAILED"


@dataclass(frozen=True)
class OrderCreated:
    order_id: str
    payment_status: PaymentStatus


class OrderService:
    def __init__(
        self,
        payment_service,
        orders_repo,
        db_pool: AsyncConnectionPool,
    ):
        self.payment_service = payment_service
        self.orders_repo = orders_repo
        self.db_pool = db_pool

    async def order(self, order) -> OrderCreated:
        self.validate_order(order)

        #must ue async here
        async with self.db_pool.connection() as conn, conn.transaction():
            order_id = await self.orders_repo.store(
                order,
                conn,
                payment_status=PaymentStatus.PENDING,
            )

            # Must INSERT into an outbox table
            # using this same DB connection.
            await self.payment_service.add_to_orders_queue(
                order_id,
                conn,
            )

        return OrderCreated(
            order_id=str(order_id),
            payment_status=PaymentStatus.PENDING,
        )

    def validate_order(self, order):
        if order is None:
            raise ValueError("Order is required")