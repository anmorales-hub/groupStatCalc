
class SystematicSamp:

    @staticmethod
    def systematicSamp(length, data):
        temp =[]
        index = 0
        while len(temp) != length:
            if index % 2 == 0:
                temp.append(data[index])
                index += 1

        return temp
