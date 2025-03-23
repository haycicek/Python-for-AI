def years_to_100(age):
    years_left = 100 - age
    return years_left

user_age = int(input("Enter your age: "))

years_left = years_to_100(user_age)
if years_left > 0:
    print(f"You will be 100 years old in {years_left} years.")
else:
    print("You have already turned 100!")
