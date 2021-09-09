class Compute:
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def add(self):
        pass

    def subtract(self):
        pass

    def divide(self):
        pass

    # adding support for multiply arithmetic
    def multiply(self):
        sum = 1
        for item in self.operands:
            sum *= item
        print(sum)
        