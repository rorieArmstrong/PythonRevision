import unittest

def div(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n

def list_squared(m, n):
    list = []
    for i in range(m,n):
        sum = 0
        for x in div(i):
            sum += x**2
        if (sum**0.5)%1 == 0:
            list.append([i, sum])
    return list

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
        self.assertEqual(list_squared(42, 250), [[42, 2500], [246, 84100]])
        self.assertEqual(list_squared(250, 500), [[287, 84100]])
