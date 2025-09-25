from __future__ import annotations

import inspect
from typing import Any, Dict

from dbt.adapters.greenplum.connections import GreenplumConnectionManager
from dbt.adapters.greenplum.connections import GreenplumCredentials
from dbt.adapters.greenplum.impl import GreenplumAdapter

try:  # dbt-core < 1.8
    from dbt.adapters.base import AdapterPlugin  # type: ignore
except ImportError:  # dbt-core >= 1.8
    from dbt.adapters.base.plugin import AdapterPlugin  # type: ignore

from dbt.include import greenplum


Plugin = AdapterPlugin(
    adapter=GreenplumAdapter,
    credentials=GreenplumCredentials,
    include_path=greenplum.PACKAGE_PATH,
    dependencies=["postgres"],
)
