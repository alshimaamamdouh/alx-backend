#!/usr/bin/env python3
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching class
    """
    def put(self, key, item):
        """ Adds data to cache
            - Args:
                - key: new entry's key
                - item: entry's value
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Gets cache data associated with given key
            - Args:
                - key to look for
            - Return:
                - value associated with the key
        """
        return self.cache_data.get(key)
