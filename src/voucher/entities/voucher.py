from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, Literal


class Voucher:
    def __init__(
        self,
        id: UUID,
        code: str,
        discount: float,
        status: Literal["active", "inactive", "expired", "maximum_use"],
        expiration_date: datetime,
        max_usage: int = 0,
        created_at: Optional[datetime] = None,
    ) -> None:
        if max_usage < 0:
            raise ValueError("max_usage cannot be negative.")
        self.id = id
        self.code = code
        self.discount = discount
        self.status = status
        self.expiration_date: datetime = expiration_date
        self.created_at = created_at or datetime.now()
        self.times_used = 0
        self.max_usage = max_usage 

    def is_valid(self) -> bool:
        if self.status != "active":
            return False
        if self.max_usage > 0 and self.times_used >= self.max_usage:
            return False
        return self.expiration_date > datetime.now()
    
    def use(self) -> None:
        if not self.is_valid():
            raise ValueError("Voucher cannot be used.")
        self.times_used += 1
        if self.max_usage > 0 and self.times_used >= self.max_usage:
            self.status = "inactive"
        
    def expire(self) -> None:
        if datetime.now() > self.expiration_date:
            self.status = 'expired'
    