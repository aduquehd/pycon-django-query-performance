from enum import Enum


class AccountTypeEnum(Enum):
    SAVINGS = "SAVINGS"
    CHECKING = "CHECKING"


class AccountStatusEnum(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class TransactionStatusEnum(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"
    CANCELED = "CANCELED"
