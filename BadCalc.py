class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1 #value 1
        self.value2 = value2 #value 2

    def add(self, value1, value2):
        return value1 + value2 #returns sum

    def subtract(self, value1, value2):
        return value1 - value2 #returns difference

    def multiply(self, value1, value2):
        i = 0 #sets i to 0\
        answer = 0 #sets answer to 0
        for i in range(value1): #makes for loop to itterate length of value 1
            answer = answer + value2 #adds value 2 to itself everytime loop executes
        return answer #returns answer


    def divide(self, value1, value2):
        count = 0

        while value1 >= value2: #compares values
            value1 -= value2 #subtracts
            count += 1 #adds to count
        remainder = value1 / value2 #calculates remainder
        return remainder + count #returns answer


value1 = 0
operation = 0
value2 = 0
value1 = int(input("Please enter your first number: "))
value2 = int(input("Please enter your second number: "))

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


