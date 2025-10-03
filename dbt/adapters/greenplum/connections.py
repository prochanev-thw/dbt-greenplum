from dataclasses import dataclass
from typing import ClassVar

try:  # dbt-core < 1.8
    from dbt.events import AdapterLogger  # type: ignore
except ImportError:  # dbt-core >= 1.8
    from dbt.adapters.events.logging import AdapterLogger  # type: ignore


from dbt.adapters.postgres.connections import PostgresCredentials, PostgresConnectionManager

logger = AdapterLogger("Greenplum")


@dataclass
class GreenplumCredentials(PostgresCredentials):
    type: ClassVar[str] = "greenplum"


class GreenplumConnectionManager(PostgresConnectionManager):
    TYPE: ClassVar[str] = "greenplum"
