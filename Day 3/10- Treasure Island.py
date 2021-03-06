#ASCII ART
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
# using 3 single quotes to print ASCII

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Ask the user whether if they want to turn left or right
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

if choice1 == "left":
        #Continue in the game. Ask the user whether if they want to wait or swim
        print("You have come to the lake.")
        choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()

        if choice2 == "wait":
             #Continue in the game. Ask the user whether if they want to red, yellow or blue door.
             print("You arrive at the island unharmed. There is a house with 3 doors. ")
             choice3 = input("One red, one yellow and one blue. Which colour do you choose?").lower()

             if choice3 == "red":
                     print("It's a room full of fire. Game over.")
             elif choice3 == "yellow":
                     print("You found a treasure! You Win!")
             elif choice3 == "blue":  
                     print("It's a room of zombie. Game over.") 
             else:      
                     print("This room doesn't exist. Game over.")               
        else:
                print("You got attacked. Game over.")   
        
else:
        print("You fell into a hole. Game over.")

# OUTPUT

'''

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

Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a crossroad, where do you want to go? Type "left" or "right". left
You have come to the lake.
Type "wait" to wait for a boat. Type "swim" to swim across. wait
You arrive at the island unharmed. There is a house with 3 doors. 
One red, one yellow and one blue. Which colour do you choose?yellow
You found a treasure! You Win!
'''
