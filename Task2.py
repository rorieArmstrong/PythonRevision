import unittest

def unique_in_order(iterable):
    list = []
    i = 0
    if type(iterable) == str:
        iterable = [i for i in iterable]
    i = 0
    list.append(iterable[i])
    while i < len(iterable)-1:
        if iterable[i+1] != iterable[i]:
            list.append(iterable[i+1])
        i += 1
    return list

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
        self.assertEqual(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])
        self.assertEqual(unique_in_order([1,2,2,3,3]), [1,2,3])
