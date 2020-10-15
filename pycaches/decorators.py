"""
Some useful caching decorators.
"""

from functools import wraps
from typing import Any, Callable

from pycaches.cache import Cache


Fany = Callable[..., Any]
Decorator = Callable[[Fany], Fany]


def cache() -> Decorator:
    """
    Make function results cachable between calls.
    """

    def decorator(function: Fany) -> Fany:
        memo: Cache[Any, Any] = Cache()

        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, kwargs)
            try:
                return memo.get(key)
            except KeyError:
                pass  # item not in cache, lets add it and return

            result = function(*args, **kwargs)
            memo.save(key, result)
            return result

        return wrapper

    return decorator
