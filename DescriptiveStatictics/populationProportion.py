from RandomNumberGenerator.listPick import ListPick


class PopulationProportion:
    @staticmethod
    def populationPorportion(seeds, nums, data):
        p = listPick.listPickListSeed(seeds, nums, data)
        pp = len(p) / len(data)
        return pp
