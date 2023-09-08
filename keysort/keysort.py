"""
Main Keysort module.

This module provides all of Keysort's functionality by exposing
functions the user is meant to utilize.
"""


from typing import Any


def keysort(my_list: list[Any], keys: list[Any] = []) -> list[Any]:
    """Sort list of dictionaries by values of multiple keys.

    Args:
        my_list (list): List of dictionaries to sort.
        keys (list): List of
    """
    if keys:
        first_key = keys[0]
        remaining_keys = keys[1:]

        presorted_list = keysort(my_list, remaining_keys)

        return sorted(presorted_list, key=lambda row: row[first_key])

    else:
        return my_list
