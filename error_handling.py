print("ERROR HANDLING PROGRAM")
print("   ")

correct_username = "Maureen"
correct_password = "1234"

try:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "" or password == "":
        raise ValueError("All fields must be filled. Login incomplete")

    if username != correct_username:
        raise NameError("Username not found. Login incomplete")

    if password != correct_password:
        raise PermissionError("Incorrect password. Login incomplete")

except ValueError as e:
    print("Error:", e)

except NameError as e:
    print("Error:", e)

except PermissionError as e:
    print("Error:", e)

else:
    print(f"Welcome, {username}! You have successfully logged in.")
    print("Login attempt complete.")
