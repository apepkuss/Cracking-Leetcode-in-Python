import unittest


class Record(object):
    def __init__(self, key):
        self.key = key

class Elements(object):
    """
    elements 14.10 Implement counting sort

    Suppose you need to reorder the elements of a very large array so that equal elements appear together. If the
    entries are integers, this reordering can be achieved by sorting the array. If the number of distinct integers
    is very small relative to the size of the array, an efficient approach to sorting the array is to count the
    number of occurrences of each distinct integer and write the appropriate number of each integer, in sorted order,
    to the array.

    You are given an array of objects. Each object has a field that is to be treated as a key. Rearrange the elements
    of the array so that objects with equal keys appear together. The order in which distinct keys appear is not
    important.
    """

    @classmethod
    def reorder_equal_subarrays(cls, records):  # O(n) time, O(n) space

        table = {}
        for record in records:
            if table.has_key(record.key):
                table[record.key][1] += 1
            else:
                table[record.key] = [-1, 1, -1]

        start_index = 0
        for value in table.values():
            value[0] = value[2] = start_index
            start_index += value[1]

        i = 0
        while i < len(records):
            key = records[i].key
            if not (table[key][0] <= i < table[key][0]+table[key][1]) or i > table[key][2]:
                records[i], records[table[key][2]] = records[table[key][2]], records[i]
                while records[table[key][2]].key == key and table[key][2] < table[key][0]+table[key][1]-1:
                    table[key][2] += 1
            else:
                if i == table[key][2] and table[key][2] < table[key][0]+table[key][1]-1:
                        table[key][2] += 1
                i += 1


class TestRun(unittest.TestCase):

    def test_case1(self):
        keys = [2,1,3,2,4,1,2,4]
        records = []
        for key in keys:
            records.append(Record(key))
        Elements.reorder_equal_subarrays(records)
        res = []
        for record in records:
            res.append(record.key)
        unittest.TestCase.assertEqual(self, first=[1,1,2,2,2,3,4,4], second=res)


if __name__ == "__main__":
    unittest.main()


