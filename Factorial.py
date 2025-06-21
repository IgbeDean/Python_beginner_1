def factorial_function(n):
    if n < 0:
        return False
    if n < 2:
        print(f"The factorial of {n}! is: 1")
        return 1
    
    product = 1
    steps = []

    for i in range(1, n + 1):
        product = product * i
        steps.append(str(i))
    
    steps_str = " x ".join(steps)
    print(f"The factorial of {n}! is: {steps_str} = {product}")
    return product

number = int(input("Enter number: "))
for i in range(number + 1):
    factorial_function(i)