import unittest

def isPrime(num):
    for i in range(2, num//2):
        if (num % i) == 0:
            return False
    return True
    

def not_primes(a, b):
    list = []
    primes = [2, 3, 5, 7]
    for i in range(a,b):
        arr = [int(d) for d in str(i)]
        if all(x in primes for x in arr):
            if not isPrime(i):
                list.append(i)
    return list


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(not_primes(2, 222), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75, 77])
        self.assertEqual(not_primes(2, 77), [22, 25, 27, 32, 33, 35, 52, 55, 57, 72, 75])
        self.assertEqual(not_primes(2700, 3000), [2722, 2723, 2725, 2727, 2732, 2733, 2735, 2737, 2752, 2755, 2757, 2772, 2773, 2775])
        self.assertEqual(not_primes(500, 999), [522, 525, 527, 532, 533, 535, 537, 552, 553, 555, 572, 573, 575, 722, 723, 725, 732, 735, 737, 752, 753, 755, 772, 775, 777])
        self.assertEqual(not_primes(999, 2500), [2222, 2223, 2225, 2227, 2232, 2233, 2235, 2252, 2253, 2255, 2257, 2272, 2275, 2277, 2322, 2323, 2325, 2327, 2332, 2335, 2337, 2352, 2353, 2355, 2372, 2373, 2375])
