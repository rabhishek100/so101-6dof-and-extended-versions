"""SO-101E teleoperator plugin entrypoint with BYOH compliance."""

from __future__ import annotations

from .config_so101e_leader import SO101ELeaderConfig
from .so101e_leader import SO101ELeader

__all__ = ["SO101ELeaderConfig", "SO101ELeader"]

_LEGACY_SUPPORT_MAX_VERSION = (0, 6, 0)


def _version_tuple(raw_version: str | None) -> tuple[int, ...]:
    if not raw_version:
        return ()

    sanitized_parts: list[int] = []
    for part in raw_version.replace("-", ".").split("."):
        digits = []
        for char in part:
            if char.isdigit():
                digits.append(char)
            else:
                break
        if not digits:
            break
        sanitized_parts.append(int("".join(digits)))

    return tuple(sanitized_parts)


def _needs_legacy_support() -> bool:
    try:
        import lerobot  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        return False

    current_version = getattr(lerobot, "__version__", "unknown")
    version_tuple = _version_tuple(current_version)
    if not version_tuple:
        return True

    return version_tuple < _LEGACY_SUPPORT_MAX_VERSION


if _needs_legacy_support():
    from . import _legacy

    _legacy.patch_make_teleoperator_from_config()
