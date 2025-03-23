numbers = []
for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

total = sum(numbers)
average = total / len(numbers)
max_value = max(numbers)
min_value = min(numbers)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Largest number: {max_value}")
print(f"Smallest number: {min_value}")