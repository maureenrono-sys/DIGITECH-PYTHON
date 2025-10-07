print("DATA BUNDLES, MINUTES, SMS MENU")
print("1. Buy Data Bundles")
print("2. Buy Minutes")
print("3. Buy SMS")
print("4. Exit")

choice = input("Select an option (1-4): ")

if choice == "1":
    print("DATA BUNDLES")
    print("1. 50MB @ KSh10")
    print("2. 200MB @ KSh20")
    print("3. 1GB @ KSh100")
    data_choice = input("Select bundle: ")

    if data_choice == "1":
        print("You have purchased 50MB for KSh10.")
    elif data_choice == "2":
        print("You have purchased 200MB for KSh20.")
    elif data_choice == "3":
        print("You have purchased 1GB for KSh100.")
    else:
        print("Invalid bundle choice.")

elif choice == "2":
    print("TUBONGE MINUTES")
    print("1. 20 Minutes @ KSh10")
    print("2. 60 Minutes @ KSh30")
    print("3. 200 Minutes @ KSh100")
    minutes_choice = input("Select bundle: ")

    if minutes_choice == "1":
        print("You have purchased 20 Minutes for KSh10.")
    elif minutes_choice == "2":
        print("You have purchased 60 Minutes for KSh30.")
    elif minutes_choice == "3":
        print("You have purchased 200 Minutes for KSh100.")
    else:
        print("Invalid bundle choice.")

elif choice == "3":
    print("SMS BUNDLES")
    print("1. 20 SMS @ KSh5")
    print("2. 100 SMS @ KSh10")
    print("3. 500 SMS @ KSh50")
    sms_choice = input("Select bundle: ")

    if sms_choice == "1":
        print("You have purchased 20 SMS for KSh5.")
    elif sms_choice == "2":
        print("You have purchased 100 SMS for KSh10.")
    elif sms_choice == "3":
        print("You have purchased 500 SMS for KSh50.")
    else:
        print("Invalid bundle choice.")

elif choice == "4":
    print("Thank you for buying bundles!")

else:
    print("Invalid choice.Kindly run the menu again.")