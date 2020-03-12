import unittest
from PopulationSampling.simpRandSamp import SimpRandSamp
from PopulationSampling.systematicSamp import SystematicSamp

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1,2,3,4,5,6]

    def test_simpRandSamp(self):
        result = SimpRandSamp.simpRandSamp(3,3, self.test)
        x = None
        for i in result:
            if i in self.test:
                x = True
            else:
                x = False
        self.assertEqual(True, x)

    def test_sysSamp(self):
        result = SystematicSamp.systematicSamp(seed=1, nums=4, data=self.test)
        self.assertEqual(result, [2, 5, 1, 3])

if __name__ == '__main__':
    unittest.main()