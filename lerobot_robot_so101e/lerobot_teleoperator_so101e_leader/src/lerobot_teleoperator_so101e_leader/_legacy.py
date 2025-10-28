"""Compatibility helpers for legacy lerobot installs."""

from __future__ import annotations

import sys
from functools import wraps
from types import ModuleType
from typing import Callable, Any

from .config_so101e_leader import SO101ELeaderConfig
from .so101e_leader import SO101ELeader

_PATCH_FLAG = "_lerobot_teleop_so101e_patched"


def _rebind_function_everywhere(original_func: Callable[..., Any], patched_func: Callable[..., Any]) -> None:
    """Replace references to ``original_func`` inside already-imported lerobot modules."""

    for module in list(sys.modules.values()):
        if not isinstance(module, ModuleType):
            continue
        module_name = getattr(module, "__name__", "")
        if not module_name or (not module_name.startswith("lerobot") and module_name != "__main__"):
            continue
        namespace = getattr(module, "__dict__", None)
        if namespace is None:
            continue
        for attr_name, attr_value in tuple(namespace.items()):
            if attr_value is original_func:
                try:
                    setattr(module, attr_name, patched_func)
                except (AttributeError, TypeError):
                    continue


def patch_make_teleoperator_from_config() -> None:
    """Patch ``lerobot``'s teleoperator factory when plugin discovery is absent."""

    try:
        from lerobot.teleoperators import utils as teleop_utils
    except ModuleNotFoundError:
        return

    original_factory = teleop_utils.make_teleoperator_from_config
    if getattr(original_factory, _PATCH_FLAG, False):
        return

    choice_name = SO101ELeaderConfig.get_choice_name(SO101ELeaderConfig)

    @wraps(original_factory)
    def patched_make_teleoperator_from_config(config):
        if getattr(config, "type", None) == choice_name:
            return SO101ELeader(config)
        return original_factory(config)

    setattr(patched_make_teleoperator_from_config, _PATCH_FLAG, True)
    teleop_utils.make_teleoperator_from_config = patched_make_teleoperator_from_config
    _rebind_function_everywhere(original_factory, patched_make_teleoperator_from_config)
