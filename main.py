import time

def adventureStart():
  
  print("Welcome to Treasure Island!")
  time.sleep(1)
  print("Your mission is to find the hidden treasure. Will you be able to find it? Good luck! \n")
  time.sleep(2)
  while 1:
      choice = input('You jump out of your sailboat. Excited to see the treasure, you run straight ahead. You stumble across a crossroad, where do you want to go? Type "Left" or "Right"').lower()
      if choice == "left":
          print("You selected left\n")
          alive = level1Left()
          return alive
          
      elif choice == "right":
          print("You selected right\n")
          alive = level1Right()
          return alive
          
      else:
          print("Error! This is not a valid response. Try again.\n")
          time.sleep(3)

def level1Left():
  print("While walking down the left path, you tripped over a tripwire and you died instantly from an arrow. GAME OVER. \n")
  time.sleep(5)
  alive = False
  return alive
  

def level1Right():
  while 1:
       choice = input('As you walk down the right path, you see a village. As you start walking closer, you see an armed guard at the gate. You ask them if you can pass. The guard said you have no reason to enter. Do you break through or walk away?   Type "Enter" or "Leave"\n').lower()
       if choice == "enter":
            print("Entered the gate\n")
            alive = level2Enter()
            return alive
            
       elif choice == "leave":
            print("Left the village\n")
            alive = level2Leave()
            return alive
            
       else:
            print("Error! This is not a valid response. Try again.\n")
            time.sleep(3)


def level2Enter():
    while 1:
        choice = input('You break through the gate anyways, the guard starts chasing you. Type: "Fight" or "Run"\n').lower()
        if choice == "fight":
            print("You chose to fight the guard.")
            alive = level2Fight()
            return alive

        elif choice == "run":
            print("You ditched the idea to fight the guard, deciding to run was a better idea.")
            alive = level2Run()
            return alive

        else:
            print("Error! This is not a valid response. Try again.\n")

def level2Fight():
  print("You turn around to fight the guard with your sword. He quickly disarms you and stabs you in the chest. Game over!\n")
  time.sleep(5)
  alive = False
  return alive

def level2Run():
    while 1:
        choice = input('You run deeper into the village with more guards gaining up on you telling you to stop. You see a huge building and a cave. Where will you go? Type "Building" or "Cave" \n').lower()
        if choice == "building":
            print("You run into the building.\n")
            alive = level2Building()
            return alive

        elif choice == "cave":
            print("You run into the cave\n")
            alive = level3Cave()
            return alive

        else:
            print("Error! This is not a valid response. Try again.\n")
            time.sleep(3)

def level3Cave():
    while 1:
        choice = print('You lose the guards in the cave, but you hear them talking about a treasure chest and requesting backup. You gotta find this chest. \n')
        time.sleep(2)
        choice = input('After searching for minutes after minutes, you see two treasure chests. You are pressured to grab one before backup arrives. Which one do you grab? Type "Right" or "Left"').lower()
        if choice == "left":
            print("You chose the left chest. \n")
            alive = level3Left()
            return alive

        elif choice == "right":
            print("You chose the right chest. \n")
            alive = level3Right()
            return alive

        else:
            print("Error! This is not a valid response. Try again.\n")

def level3Left():
    print('Now running with the chest on the left, you find a hidden passage. You go through that passage and you escape the village. You laugh and put your hands on the lock. \n')
    time.sleep(1)
    print('You feel a sharp pain in your neck, you look down and see a sword in your neck. You black out. Game over!')
    alive = False
    return alive

def level3Right():
    print('Now running with the chest on the right, you find a hidden passage. You go through that passage and you escape the village. You laugh and put your hands on the lock. \n')
    time.sleep(1)
    print('You see gold and many riches in the chest. You walk back to your ship with a smile on your face. You win!')
    alive = True
    return alive

def level2Building():
        while 1:
            choice = input('You walk into the building and it so happened to be the king\'s building. You beg the king for help and the king calls off the guards. The king is confused, and he wants to know why you are here. Do you lie or tell the truth? Type "Lie" or "Truth"\n').lower()
            if choice == "lie":
                print("You decided to lie. \n")
                alive = level3Lie()
                return alive

            elif choice == "truth":
                print("You decided to tell the truth \n")
                alive = level3Truth()
                return alive

            else:
                print("Error! This is not a valid response. Try again.\n")

def level3lie():
    print('You said you were visiting the village, wanting to live here.\n')
    time.sleep(1)
    print('The king stares at you. He pulls out a baton and knocks you out cold. You wake up in a jail cell. Game over!')
    alive = False
    return alive

def level3Truth():
    print('You said you were trying to steal the treasure in the village. You apologized to the king over and over again\n')
    time.sleep(1)
    print('The king laughs and appreciates your honesty. He reaches in his pocket and gives you a ruby. He tells you to never come back.')
    time.sleep(3)
    print("You leave the village and walk back to the ship. Game over, but this isn\'t the best ending. Play again!")
    alive = False
    return alive


def level2Leave():
  print("You decide you don't want to bother entering")
  alive = level4forest
  return alive

def level4forest():
    while 1:
        choice = input("You wonder aimlessly in the forest. You once again see two different paths. A straight path and a curved path. Where do you go?").lower()
        if choice == "straight":
            print("You decided to go down the straight path. \n")
            alive = level4straight()
            return alive

        elif choice == "curve":
            print("You decided to the curved path \n")
            alive = level4curve()
            return alive

        else:
            print("Error! This is not a valid response. Try again.\n")

def level4straight():
    print("While walking down the straight path, you activated a trap. You fell into a hole and you are stuck there forever. Game over!")
    alive = False
    return alive

def level4curve():
    print("While walking down the curve path, a bear comes out of nowhere and attacks you. You don't put up much of a fight and you die. Game over!")
    alive = False
    return alive
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
  alive = adventureStart()
  if alive:
    break

