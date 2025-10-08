# Performing the for loop in a program

for number in range(10):
    print(number * "*")

# even numbers
for number in range(10):
    if number %2 == 0:
        print(number * "*")

for number in range(2,10):
    if number %2 == 0:
        print(number)

for number in range(10):
    if number %2 == 0:
        print(number)

# odd numbers
for number in range(10):
    if number %2 == 1:
        print(number)

# we are performing the while loop in our programs
# Access control
trial = 3
attempt = 0

while attempt < trial:
    value = input("Enter password:  ")
    if value == "Maureen1234":
        print("Login successful!!")
        break
    else: 
        print("Wrong password. Try again!!")
        attempt +=1

else: 
    print("You failed. Number of attempts are over!!")
        