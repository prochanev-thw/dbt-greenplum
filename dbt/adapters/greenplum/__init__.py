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


def _plugin_kwargs() -> Dict[str, Any]:
    signature = inspect.signature(AdapterPlugin)
    params = signature.parameters

    kwargs: Dict[str, Any] = {
        "adapter": GreenplumAdapter,
        "credentials": GreenplumCredentials,
        "include_path": greenplum.PACKAGE_PATH,
        "dependencies": ["postgres"],
    }

    name_keys = ("name", "adapter_name", "adapter_type")
    for key in name_keys:
        if key in params:
            kwargs[key] = "greenplum"
            break

    return kwargs


Plugin = AdapterPlugin(**_plugin_kwargs())
