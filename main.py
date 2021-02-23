print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
while 1:
    print("Welcome to Treasure Island!")
    print("Your mission is to find the hidden treasure. Will you be able to find it?") 
    wrongchoice = True
    alive = True
    while wrongchoice and alive:
       choice1 = input('You jump out of your sailboat. Excited to see the treasure, you run straight ahead. You stumble across a crossroad, where do you want to go? Type "Left" or "Right" ').lower()
       if choice1 == "left":
            print("You selected left")
            print("You died! \n")
            alive = False
       elif choice1 == "right":
            print("You selected right")
            break
       else:
            print("Error! This is not a valid response. Try again. ")

    

    while wrongchoice and alive:
       choice2 = input("This is the next part of the game. Where will you go?").lower()
       if choice2 == "left":
            print("1")
            break
       elif choice2 == "right":
            print("2")
            break
       else:
            print("Error! This is not a valid response. Try again. ")

