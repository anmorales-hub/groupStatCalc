class Calculator:
    Result = 0
    def __init__(self):
        pass
    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Multiplication(self, a, b):
        self.Result = Multiplication.multiplication(a, b)
        return self.Result

