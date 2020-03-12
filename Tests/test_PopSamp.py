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

    def test_systematicSamp(self):
        result = SystematicSamp.systematicSamp(3,self.test)
        self.assertEqual([2,4,6], result)

if __name__ == '__main__':
    unittest.main()