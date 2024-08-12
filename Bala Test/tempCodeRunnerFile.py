while True:
    type_choice = int(input("Enter your age: "))
        # Some conditions here
    if type_choice == 19:
        print("Spot on.")
        break
    if type_choice >= 93:
        print("You are very old")
    elif 85 <= type_choice <= 92:
        print("You are close to dying")
    elif 34 <= type_choice <= 85:
        print("You are the golden age")
    elif 20 <= type_choice < 34:
        print("You are living your best life")