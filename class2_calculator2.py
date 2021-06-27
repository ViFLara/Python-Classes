class Calculator2:

    # def __init__(self):
    #     pass

    def sum(self, value_a, value_b):
        return value_a + value_b

    def subtraction(self, value_a, value_b):
        return value_a - value_b

    def multiplication(self, value_a, value_b):
        return value_a * value_b

    def division(self, value_a, value_b):
        return value_a / value_b


calculator = Calculator2()
print(calculator.sum(10, 2))
print(calculator.subtraction(5, 3))
print(calculator.multiplication(100, 2))
print(calculator.division(10, 5))
