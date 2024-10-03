def solve_exercise2():
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    if height >= 120:
        print("You can ride the rollercoaster")
        age = int(input("What is your age?"))
        if age<12:
            print("Please pay $5")
        elif age<=18:
            print("Please pay $7")
        else:
            print("Please pay $12")
    else:
        print("You can not ride the rollercoaster")

    number = int(input("Enter your number: "))
    if number%2 == 1 :
        print("Odd")
    else:
        print("Even")

    print("Welcome to python Pizza Deliveries!")
    size = input("What size of pizza do you want? S, M or L: ")
    pepperoni = input("Do you want to pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want to extra cheese? Y or N: ")

    price = 0

    if size == "S":
        price = 15
        if pepperoni == "Y":
            price += 2
                       
    elif size == "M":
        price = 20
        if pepperoni == "Y":
            price += 3
        
    elif size == "L":
        price = 25
        if pepperoni == "Y":
            price += 3
        
    else:
        print("Your input is incorrect")

    if extra_cheese == "Y":
        price += 1

    print(f"Your amount is: {price}")

    

    
