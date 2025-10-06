# This programe checks on the user inputs and validates it

print("This program needs the credentials to be verified before granting access to users")
print()


username = input("Enter your username:  ")
password = input("Enter password:  ")

if username == "Maureen" and password == "maureen12345":
    print("Signed in successfully!")

elif username != "maureen12345" and password == "maureen12345":
    print("Check your credentials and try again!!")
    
else:
    print("Wrong credentials")