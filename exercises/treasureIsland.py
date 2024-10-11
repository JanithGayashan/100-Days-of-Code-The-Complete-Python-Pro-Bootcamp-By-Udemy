def treasure_island():
    print('''*******************************************************************************
        |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************
        ''')
    
    print("Welcome to Treasure Island Game.\n Your mission is to find the treasure.")
    first_selection = input("You want to choose Left or Right: ")
    if (first_selection == "Left"):
        print("Now you are in the next step.")
        second_selection = input("You want to choose Swim or Wait: ")
        if (second_selection == "Wait"):
            print("Now you are in the next phase.")
            third_selection = input("This is the final phase. You want to selct Red, Yellow or Blue: ")
            if third_selection == "Yellow":
                print("You Win!")
            elif third_selection == "Red":
                print("Burned by fire. \n Game Over.")
            else:
                print("Eaten by beasts. \n Game Over.")
        else:
            print("Attacked by trout. \n Game Over.")
    else:
        print("Fall into the hole. \n Game Over.")
    