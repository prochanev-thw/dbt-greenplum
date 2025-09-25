from dataclasses import dataclass
from typing import ClassVar

from dbt.events import AdapterLogger
from dbt.adapters.postgres.connections import (
    PostgresConnectionManager,
    PostgresCredentials,
)

logger = AdapterLogger("Greenplum")


@dataclass
class GreenplumCredentials(PostgresCredentials):
    type: ClassVar[str] = "greenplum"


class GreenplumConnectionManager(PostgresConnectionManager):
    TYPE: ClassVar[str] = "greenplum"
