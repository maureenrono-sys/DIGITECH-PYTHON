print("=== SYSTEM LOGIN ===")

username = input("Enter username: ")
password = input("Enter password: ")
role = input("Enter role:  ")

if username == " " and password == " " and role == "Admin":
    print("You have FULL access to the system.")
    print("Features: View data, Edit data, Delete data, Manage users")

elif username == " " and password == " " and role == "Staff":
    print("You have LIMITED access.")
    print("Features: View data, Edit data")

elif username == " " and password == " " and role == "Guest":
    print("You have VIEW-ONLY access.")
    print("Features: View data only")

else:
    print("Access denied.")