def calculator(a, b):
    total = a + b
    difference = a - b
    product = a * b
    if b != 0:
        division = a / b
    else:
        division = "Undefined (division by zero)"
    
    return total, difference, product, division

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculator(num1, num2)

print(f"Total: {result[0]}")
print(f"Difference: {result[1]}")
print(f"Product: {result[2]}")
print(f"Division: {result[3]}")