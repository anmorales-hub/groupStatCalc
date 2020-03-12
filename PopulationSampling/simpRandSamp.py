import random
from RNG.listPick import ListPick

class SimpRandSamp:

    @staticmethod
    def simpRandSamp(seed,nums,data):
        random.seed(seed)
        return ListPick.listPickListSeed(seed,nums,data)