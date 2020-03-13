from RNG.listPick import ListPick

class SystematicSamp:

    @staticmethod
    def systematicSamp(seed,nums, data):
        return ListPick.listPickListSeed(seed,nums,data)