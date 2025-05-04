def calculator():
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /, %, **, //, **0.5, pow,abs, round, max, min, divmod): ")
    b = float(input("Enter second number: "))

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    elif op == '%':
        print("Result:", a % b)
    elif op == '**':
        print("Result:", a ** b)
    elif op == '//':
        print("Result:", a // b)
    elif op == 'sqrt':
        print("Result:", a ** 0.5)
    elif op == 'pow':
        print("Result:", pow(a, b))
    elif op == 'abs':
        print("Result:", abs(a))
    elif op == 'round':
        print("Result:", round(a))
    elif op == 'max':
        print("Result:", max(a, b))
    elif op == 'min':
        print("Result:", min(a, b))
    elif op == 'divmod':
        print("Result:", divmod(a, b))

    else:
        print("Invalid operator.")

calculator()
