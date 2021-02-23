import time

def adventureStart():
  
  print("Welcome to Treasure Island!")
  print("Your mission is to find the hidden treasure. Will you be able to find it?") 
  while 1:
      choice = input('You jump out of your sailboat. Excited to see the treasure, you run straight ahead. You stumble across a crossroad, where do you want to go? Type "Left" or "Right" ').lower()
      if choice == "left":
          print("You selected left\n")
          alive = level1Left()
          return alive
          
      elif choice == "right":
          print("You selected right")
          alive = level1Right()
          return alive
          
      else:
          print("Error! This is not a valid response. Try again.\n")

def level1Left():
  print("While walking down the left path, you tripped over a tripwire and you died instantly from an arrow. GAME OVER. \n")
  time.sleep(5)
  alive = False
  return alive
  

def level1Right():
  while 1:
       choice = input('As you walk down the right path, you see a village. As you start walking closer, you see an armed guard at the gate. You ask them if you can pass. The guard said you have no reason to enter. Do you break through or walk away?   Type "Enter" or "Leave"').lower()
       if choice == "enter":
            print("Entered the gate")
            alive = level2Enter()
            return alive
            
       elif choice == "leave":
            print("Left the village")
            alive = level2Leave()
            return alive
            
       else:
            print("Error! This is not a valid response. Try again. ")

def level2Fight():
  print("The guard beats your ass")
  alive = False
  return alive

def level2Treasure():
  print("You quickly steal the treasure and bail")
  alive = True
  return alive

def level2Enter():
  while 1:
       choice = input('You break through the gate anyways, the guard starts chasing you. Type: "Fight" or "Treasure"').lower()
       if choice == "fight":
            alive = level2Fight()
            return alive
       elif choice == "treasure":
            alive = level2Treasure
            return alive
        
       else:
            print("Error! This is not a valid response. Try again. ")

def level2Leave():
  #work in progress modify as needed
  print("inside leaving village function")
  alive = True
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

