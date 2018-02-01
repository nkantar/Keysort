import unittest

from keysort import keysort


class MultisortTest(unittest.TestCase):
    def setUp(self):
        self.sorted_list = [
            {'col1': 'a', 'col2': '1', 'col3': 'A'},
            {'col1': 'a', 'col2': '1', 'col3': 'B'},
            {'col1': 'a', 'col2': '2', 'col3': 'A'},
            {'col1': 'a', 'col2': '2', 'col3': 'B'},
            {'col1': 'b', 'col2': '1', 'col3': 'A'},
            {'col1': 'b', 'col2': '1', 'col3': 'B'},
            {'col1': 'b', 'col2': '2', 'col3': 'A'},
            {'col1': 'b', 'col2': '2', 'col3': 'B'},
            {'col1': 'c', 'col2': '1', 'col3': 'A'},
            {'col1': 'c', 'col2': '1', 'col3': 'B'},
            {'col1': 'c', 'col2': '2', 'col3': 'A'},
            {'col1': 'c', 'col2': '2', 'col3': 'B'},
            {'col1': 'd', 'col2': '1', 'col3': 'A'},
            {'col1': 'd', 'col2': '1', 'col3': 'B'},
            {'col1': 'd', 'col2': '2', 'col3': 'A'},
            {'col1': 'd', 'col2': '2', 'col3': 'B'},
        ]

        self.unsorted_list = [
            {'col1': 'a', 'col2': '2', 'col3': 'A'},
            {'col1': 'd', 'col2': '2', 'col3': 'A'},
            {'col1': 'b', 'col2': '1', 'col3': 'B'},
            {'col1': 'a', 'col2': '2', 'col3': 'B'},
            {'col1': 'b', 'col2': '1', 'col3': 'A'},
            {'col1': 'b', 'col2': '2', 'col3': 'B'},
            {'col1': 'd', 'col2': '1', 'col3': 'B'},
            {'col1': 'a', 'col2': '1', 'col3': 'B'},
            {'col1': 'c', 'col2': '2', 'col3': 'B'},
            {'col1': 'c', 'col2': '2', 'col3': 'A'},
            {'col1': 'c', 'col2': '1', 'col3': 'B'},
            {'col1': 'c', 'col2': '1', 'col3': 'A'},
            {'col1': 'b', 'col2': '2', 'col3': 'A'},
            {'col1': 'a', 'col2': '1', 'col3': 'A'},
            {'col1': 'd', 'col2': '2', 'col3': 'B'},
            {'col1': 'd', 'col2': '1', 'col3': 'A'},
        ]

    def test_sort(self):
        my_sorted_list = keysort(self.unsorted_list, ['col1', 'col2', 'col3'])

        self.assertEquals(my_sorted_list, self.sorted_list)


if __name__ == '__main__':
    unittest.main()
