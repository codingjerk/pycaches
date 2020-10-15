"""
A bunch of caches.
"""

from pycaches.nohashmap import Map
from pycaches.cache import Cache
from pycaches.decorators import cache


__all__ = ["cache", "Cache", "Map"]
