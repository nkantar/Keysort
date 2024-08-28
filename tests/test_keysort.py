from keysort import keysort


SORTED_LIST = [
    {"col1": "a", "col2": "1", "col3": "A"},
    {"col1": "a", "col2": "1", "col3": "B"},
    {"col1": "a", "col2": "2", "col3": "A"},
    {"col1": "a", "col2": "2", "col3": "B"},
    {"col1": "b", "col2": "1", "col3": "A"},
    {"col1": "b", "col2": "1", "col3": "B"},
    {"col1": "b", "col2": "2", "col3": "A"},
    {"col1": "b", "col2": "2", "col3": "B"},
    {"col1": "c", "col2": "1", "col3": "A"},
    {"col1": "c", "col2": "1", "col3": "B"},
    {"col1": "c", "col2": "2", "col3": "A"},
    {"col1": "c", "col2": "2", "col3": "B"},
    {"col1": "d", "col2": "1", "col3": "A"},
    {"col1": "d", "col2": "1", "col3": "B"},
    {"col1": "d", "col2": "2", "col3": "A"},
    {"col1": "d", "col2": "2", "col3": "B"},
]

UNSORTED_LIST = [
    {"col1": "a", "col2": "2", "col3": "A"},
    {"col1": "d", "col2": "2", "col3": "A"},
    {"col1": "b", "col2": "1", "col3": "B"},
    {"col1": "a", "col2": "2", "col3": "B"},
    {"col1": "b", "col2": "1", "col3": "A"},
    {"col1": "b", "col2": "2", "col3": "B"},
    {"col1": "d", "col2": "1", "col3": "B"},
    {"col1": "a", "col2": "1", "col3": "B"},
    {"col1": "c", "col2": "2", "col3": "B"},
    {"col1": "c", "col2": "2", "col3": "A"},
    {"col1": "c", "col2": "1", "col3": "B"},
    {"col1": "c", "col2": "1", "col3": "A"},
    {"col1": "b", "col2": "2", "col3": "A"},
    {"col1": "a", "col2": "1", "col3": "A"},
    {"col1": "d", "col2": "2", "col3": "B"},
    {"col1": "d", "col2": "1", "col3": "A"},
]


def test_keysort() -> None:
    assert keysort(UNSORTED_LIST, ["col1", "col2", "col3"]) == SORTED_LIST
