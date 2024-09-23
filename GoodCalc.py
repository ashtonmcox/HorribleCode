class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

value1 = float(input("Please enter your first number: "))
value2 = float(input("Please enter your second number: "))

calculator = Calculator(value1, value2)

print("Please choose an operation from the options below")
print("Operations")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input())

if(operation == 1):
    print(calculator.add(value1, value2))
elif(operation == 2):
    print(calculator.subtract(value1, value2))
elif(operation == 3):
    print(calculator.multiply(value1, value2))
elif(operation == 4):
    print(calculator.divide(value1, value2))
else:
    print("Please try again with a valid operation")


