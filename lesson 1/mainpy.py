# Интерфейс
from lesson1 import add, substract, multiply, divide

print("Калькулятор:")

a = float(input("a = "))
operation = input("+, -, *, /")
b = float(input("b = "))

if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = substract(a,b)
elif operation == "*":
    result = multiply(a, b)
elif operation == "/":
    result = divide(a, b)

else:
    print("We don't know this operation")
    result = None

print(f"Result: {result}")