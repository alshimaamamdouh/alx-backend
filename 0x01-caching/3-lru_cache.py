#!/usr/bin/env python3
"""
LIFO caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict
from typing import Any, Optional


class LRUCache(BaseCaching):
    """ LIFO cache class
    """
    def __init__(self):
        """ Initialize new instance
        """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key: Any, item: Any) -> None:
        """ Adds data to cache based on LRU policy
            - Args:
                - key: new entry's key
                - item: entry's value
        """
        if not key or not item:
            return
        new_cache_data = {key: item}
        if len(self.cache_data) == self.MAX_ITEMS:
            key_to_remove = list(self.cache_data.keys())[-1]
            self.cache_data.pop(key_to_remove)
            print(f'DISCARD: {key_to_remove}')
        self.cache_data.update(new_cache_data)
        self.cache_data.move_to_end(key, last=False)

    def get(self, key: Any) -> Optional[Any]:
        """ Gets cache data associated with given key
            - Args:
                - key to look for
            - Return:
                - value associated with the key
        """
        cache_item = self.cache_data.get(key)
        if cache_item:
            self.cache_data.move_to_end(key, last=False)
        return cache_item
