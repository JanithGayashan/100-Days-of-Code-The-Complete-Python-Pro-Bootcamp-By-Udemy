# exercises/exercise1.py
def solve_exercise1():
    print("Solving Exercise 1")
    name = "sunil"
    print(name[2])
    print(name[-1])

    total = 150
    newTotal = 200

    print(total)
    print(newTotal)
    print(total + newTotal)

    bill = 100.75 #this is the floating data type
    print(bill)
    
    bool_name = True
    print(bool_name)

    print(False)
    
    # type checking
    print(type("This is String datatype")) #type() is inbuild fuction like len function
    print(type(1234))
    print(type(350.84))
    print(type(True))

    name = input("Enter your name")
    length_name = len(name)
    print("Number of letters in your name: " + str(length_name))

    # bmi calculator
    height = 1.65
    weight = 84

    bmi = weight/(height**2)
    print(bmi)

    print("Welcome to the tip calculator!")
    total_bill = float(input("What is the total bill?")) #all inputs are get in as string so we want to type conversion into float or int 
    tip = int(input("How much tip would like to give? 10, 12, or 15?"))
    split_size = int(input("How many people to split the bil?"))
    pay_person = (total_bill + total_bill*tip/100)/split_size
    print(pay_person)