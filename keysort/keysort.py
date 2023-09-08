"""
Main Keysort module.

This module provides all of Keysort's functionality by exposing
functions the user is meant to utilize.
"""


from typing import Any, List


def keysort(my_list: List[Any], keys: List[Any] = []) -> List[Any]:
    """Sort list of dictionaries by values of multiple keys.

    Args:
        my_list (list): List of dictionaries to sort.
        keys (list): List of keys by which to sort.

    Returns:
        list: Sorted list of dictionaries.

    """
    if keys:
        first_key = keys[0]
        remaining_keys = keys[1:]

        presorted_list = keysort(my_list, remaining_keys)

        return sorted(presorted_list, key=lambda row: row[first_key])

    else:
        return my_list
