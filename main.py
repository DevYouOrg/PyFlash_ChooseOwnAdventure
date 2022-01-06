
# EXERCISE ONE
print("I am a software developer!")

# EXERCISE TWO
fave_color = input("Enter your favorite color")
print(fave_color)

#Challenge
print(f"Your favorite color is {fave_color}")


# EXERCISE THREE
age = input("Enter age: ")

if age > 21:
    print("Your age is greater than 21")
if age == 21:
    print("Your age is 21")
if age < 21:
    print("Your age is less than 21")

# EXERCISE FOUR
password = "1234"
user_input = input("Enter password: ")

if user_input == password:
    print("You have access!")
else:
    print("You do not have access!")

# EXERCISE FIVE
password = "1234"

user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

    if user_input == password:
        print("You have access!")
