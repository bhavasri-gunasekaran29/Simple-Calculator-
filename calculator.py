def calculator(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"


while True:
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    result = calculator(a, operator, b)
    print("Result:", result)

    choice = input("Do you want to calculate again? (yes/no): ")

    if choice.lower() != "yes":
        print("Calculator closed.")
        break