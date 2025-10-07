print("SYSTEM LOGIN")

users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "staff": {"password": "staff123", "role": "Staff"},
    "guest": {"password": "guest123", "role": "Guest"}
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username]["password"] == password:
    role = users[username]["role"]
    print(f"Login successful! Welcome, {username}. Your role is: {role}")

    if role == "Admin":
        print("You have FULL access to the system.")
        print("Features: View data, Edit data, Delete data, Manage users")

    elif role == "Staff":
        print("You have LIMITED access.")
        print("Features: View data, Edit data")

    elif role == "Guest":
        print("You have VIEW-ONLY access.")
        print("Features: View data only")

else:
    print("Access Denied! Invalid username or password.")