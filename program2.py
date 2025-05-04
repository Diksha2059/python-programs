def add_numbers(a, b, c):
    return a + b + c

def multiply_numbers(a, b, c):
    return a * b * c

def divide_numbers(a, b, c):
    if b == 0 or c == 0:
        return "Division by zero is not allowed"
    return a / b / c

def subtract_numbers(a, b, c):
    return a - b - c

# Example usage
num1 = 10
num2 = 5
num3 = 2

print("Addition:", add_numbers(num1, num2, num3))
print("Multiplication:", multiply_numbers(num1, num2, num3))
print("Division:", divide_numbers(num1, num2, num3))
print("Subtraction:", subtract_numbers(num1, num2, num3))