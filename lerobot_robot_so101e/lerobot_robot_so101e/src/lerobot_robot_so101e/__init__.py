"""SO-101E follower plugin entrypoint.

The package layout follows Hugging Face's "Bring Your Own Hardware" guide so
that modern versions of ``lerobot`` can discover it automatically.  For older
releases (pre-0.6), we still apply a small compatibility shim that registers
the robot factory dynamically.
"""

from __future__ import annotations

from .config_so101e_follower import SO101EFollowerConfig
from .so101e_follower import SO101EFollower

__all__ = ["SO101EFollowerConfig", "SO101EFollower"]

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
        # Importing docs/tests without lerobot in the environment.
        return False

    current_version = getattr(lerobot, "__version__", "unknown")
    version_tuple = _version_tuple(current_version)
    if not version_tuple:
        # Unknown/dev version -> assume legacy behavior.
        return True

    return version_tuple < _LEGACY_SUPPORT_MAX_VERSION


if _needs_legacy_support():
    from ._legacy import patch_make_robot_from_config

    patch_make_robot_from_config()
