number = int(input("Please enter a number between 1 and 100: "))
x = 1

while x <= number:
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
    x += 1




