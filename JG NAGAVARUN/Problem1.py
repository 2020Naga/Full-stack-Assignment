

class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'addition' or self.operation == 'add' or self.operation == '+':
            return self.a + self.b
        elif self.operation == 'subtraction' or self.operation == 'subtract' or self.operation == '-':
            return self.a - self.b
        elif self.operation == 'multiplication' or self.operation == 'multiply' or self.operation == '*':
            return self.a * self.b
        elif self.operation == 'division' or self.operation == 'divide' or self.operation == '/':
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Error: Invalid Operation"


if __name__ == "__main__":
    calc = Calculator(10.5, 2.5, "Addition")
    print(calc.calculate())  # Output: 13.0