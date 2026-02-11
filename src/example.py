from typing import Iterable

if TYPE_CHECKING:
    from collections.abc import Iterable


def m() -> Iterable:
    """Magic function."""
    return "Hello world"
