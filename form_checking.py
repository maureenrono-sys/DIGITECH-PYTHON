print("USER REGISTRATION FORM")

name = input("Enter your full name: ")
age = input("Enter your age: ")
email = input("Enter your email address: ")

if name == "":
    print("Error: Name cannot be empty.")

elif age == "":
    print("Error: Age cannot be empty.")

elif email == "":
    print("Error: Email cannot be empty.")

else:
    print("")
    print("Form submitted successfully!")
    print(f"Name:", name)
    print(f"Age:", age)
    print(f"Email:", email)