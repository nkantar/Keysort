from dataclasses import dataclass

from keysort import attrsort


@dataclass
class MyObj:
    col1: str
    col2: str
    col3: str


SORTED_LIST = [
    MyObj(col1="a", col2="1", col3="A"),
    MyObj(col1="a", col2="1", col3="B"),
    MyObj(col1="a", col2="2", col3="A"),
    MyObj(col1="a", col2="2", col3="B"),
    MyObj(col1="b", col2="1", col3="A"),
    MyObj(col1="b", col2="1", col3="B"),
    MyObj(col1="b", col2="2", col3="A"),
    MyObj(col1="b", col2="2", col3="B"),
    MyObj(col1="c", col2="1", col3="A"),
    MyObj(col1="c", col2="1", col3="B"),
    MyObj(col1="c", col2="2", col3="A"),
    MyObj(col1="c", col2="2", col3="B"),
    MyObj(col1="d", col2="1", col3="A"),
    MyObj(col1="d", col2="1", col3="B"),
    MyObj(col1="d", col2="2", col3="A"),
    MyObj(col1="d", col2="2", col3="B"),
]

UNSORTED_LIST = [
    MyObj(col1="a", col2="2", col3="A"),
    MyObj(col1="d", col2="2", col3="A"),
    MyObj(col1="b", col2="1", col3="B"),
    MyObj(col1="a", col2="2", col3="B"),
    MyObj(col1="b", col2="1", col3="A"),
    MyObj(col1="b", col2="2", col3="B"),
    MyObj(col1="d", col2="1", col3="B"),
    MyObj(col1="a", col2="1", col3="B"),
    MyObj(col1="c", col2="2", col3="B"),
    MyObj(col1="c", col2="2", col3="A"),
    MyObj(col1="c", col2="1", col3="B"),
    MyObj(col1="c", col2="1", col3="A"),
    MyObj(col1="b", col2="2", col3="A"),
    MyObj(col1="a", col2="1", col3="A"),
    MyObj(col1="d", col2="2", col3="B"),
    MyObj(col1="d", col2="1", col3="A"),
]


def test_attrsort() -> None:
    assert attrsort(UNSORTED_LIST, ["col1", "col2", "col3"]) == SORTED_LIST
