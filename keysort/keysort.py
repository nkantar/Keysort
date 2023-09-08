from typing import Any


def keysort(my_list: list[Any], keys: list[Any] = []) -> list[Any]:
    if keys:
        first_key = keys[0]
        remaining_keys = keys[1:]

        presorted_list = keysort(my_list, remaining_keys)

        return sorted(presorted_list, key=lambda row: row[first_key])

    else:
        return my_list
