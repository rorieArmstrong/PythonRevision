import unittest

def title_case(title, minor_words=''):
    minor = minor_words.split()
    arr = (title.capitalize()).split()
    res = ''
    for i in range(0,len(arr)):
        if i != 0:
            res += ' '
        if arr[i] not in minor:
            res += str(arr[i]).capitalize()
        else:
            res += str(arr[i]).lowercase()
    return res
        
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(title_case(''), '')
        self.assertEqual(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
        self.assertEqual(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
        self.assertEqual(title_case('the quick brown fox'), 'The Quick Brown Fox')
