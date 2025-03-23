age = int(input("Enter your age: "))

# Determine the age group
if 0 <= age <= 12:
    age_group = "Child"
elif 13 <= age <= 19:
    age_group = "Teen"
elif 20 <= age <= 59:
    age_group = "Adult"
elif age >= 60:
    age_group = "Senior"
else:
    age_group = "Invalid age!"

print(f"Your age group is: {age_group}")