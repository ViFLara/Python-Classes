class Calculator:

    # function
    def __init__(self, num1, num2):
        self.value_a = num1
        self.value_b = num2

    def sum(self):
        return self.value_a + self.value_b

    def subtraction(self):
        return self.value_a - self.value_b

    def multiplication(self):
        return self.value_a * self.value_b

    def division(self):
        return self.value_a / self.value_b

calculator = Calculator(10, 2)
print(calculator.value_a)
print(calculator.value_b)
print(calculator.sum())
print(calculator.subtraction())
print(calculator.multiplication())
print(calculator.division())
