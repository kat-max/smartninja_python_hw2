print("Hello kind stranger! Welcome to the program that converts units. More specifically, kilometers into miles. Wanna see?")

while True:
    km = int(input("Please enter any number of kilomteres that you would like to convert into miles: "))
    miles = km * 0.621371192
    print(f"{km} kilometers is {miles} miles.")
    answer = input("Would you like to do another conversion (yes/no)? ")
    if answer.lower() != "yes" and answer.lower() != "y":
        print("Ok, thank you and have a nice day!")
        break








