"""
Main Keysort module.

This module provides all of Keysort's functionality by exposing
functions the user is meant to utilize.
"""


from typing import Any, List, Callable


def _multisort(
    call_func: Callable[..., Any],
    key_func: Callable[..., Any],
    my_list: List[Any],
    keys: List[Any] = [],
) -> List[Any]:
    if keys:
        first_key = keys[0]
        remaining_keys = keys[1:]

        presorted_list = call_func(my_list, remaining_keys)

        return sorted(presorted_list, key=lambda row: key_func(row, first_key))

    else:
        return my_list


def keysort(my_list: List[Any], keys: List[Any] = []) -> List[Any]:
    """Sort list of dictionaries by values of multiple keys.

    Args:
        my_list (list): List of dictionaries to sort.
        keys (list): List of keys by which to sort.

    Returns:
        list: Sorted list of dictionaries.

    """
    return _multisort(keysort, dict.get, my_list, keys)


def attrsort(my_list: List[Any], attrs: List[Any] = []) -> List[Any]:
    """Sort list of objects by values of multiple attributes.

    Args:
        my_list (list): List of objects to sort.
        attrs (list): List of attributes by which to sort.

    Returns:
        list: Sorted list of objects.

    """
    return _multisort(attrsort, getattr, my_list, attrs)
