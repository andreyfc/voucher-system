from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

UUID()


class Voucher:
    def __init__(
        self,
        id: UUID,
        code: str,
        discount: float,
        is_active: bool,
        expiration_date: datetime,
        created_at: Optional[datetime] = None,
    ) -> None:
        self.id = id,
        self.code = code,
        self.discount = discount,
        self.is_active = is_active,
        self.expiration_date: datetime = expiration_date,
        self.created_at = created_at or datetime.now()

