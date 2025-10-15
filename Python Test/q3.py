username = input("Enter username: ")
password = input("Enter password: ")

if password == ("python123"):
    print("Access granted")

while password != ("python123"):
    print("Access denied. Try again later.")

else:
    print("Attempt failed")

