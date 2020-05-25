import unittest

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    res = []
    for i in range(a,b+1):
        list = [int(j) for j in str(i)]
        sum = 0
        k = 0
        while k < len(list):
            sum += list[k]**(k+1)
            k +=1
            if int(sum) == int(i):
                res.append(sum)            
    return res

class Test(unittest.TestCase):
    def test(self):
        self.assertEquals(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEquals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        self.assertEquals(sum_dig_pow(10, 89),  [89])
        self.assertEquals(sum_dig_pow(10, 100),  [89])
        self.assertEquals(sum_dig_pow(90, 100), [])
        self.assertEquals(sum_dig_pow(89, 135), [89, 135])