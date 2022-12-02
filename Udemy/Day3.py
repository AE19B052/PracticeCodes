'''
Treasure Hunt Game
'''

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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

decision_1 = input("You are front of a river\n. You can got three ways: right, left or jump into river\n. Type your decision (Allowed entries are right, left or jump).\t").lower()
if decision_1 == 'right':
    decision_r1 = input("After walking a long way, you saw it's sunset time.\nWhat do you want to do. 'Camp here and rest' or 'continue of eating'.\nType your decision (Allowed entries are:- camp or continue)\t").lower()
    if decision_1 == 'continue':
        print("You after 1 mile there was a cliff you didn't saw it. You fell and die.\nGAME OVER!")
    elif decision_r1 == 'camp':
        decision_r2 = input("You woke up and started walking. After a while you reached a cliff, You realized that yesterday's decision was correct.\nNow only option you have is to jump in river or quit the hunt.\nAcceptable reponses are:- quit or jump.\t").lower()
        if decision_r2 == 'jump':
            print('River is full of crocodile. Your became there food.\nGAME OVER!')
        elif decision_r2 == 'quit':
            print("GAME OVER!")
        else:
            print('Invalid Input.\nGAME OVER!')
    else:
        print("Can't accept the input.\nGAME OVER!")
elif decision_1 == 'jump':
    print('River is full of crocodile. Your became there food.\nGAME OVER!')

elif decision_1 == 'left':
    decision_l1 = input("You came across board which address 'Boats are used for crossing. Please wait for boat'.\n Make a choose 'jump and cross' or 'wait for boat'.\nAllowed inputs are:- jump or wait.\t").lower()
    if decision_l1 == 'jump':
        print('River is full of crocodile. Your became there food.\nGAME OVER!')
    elif decision_l1 == 'wait':
        decision_l2 = input("After a waiting, Boat arrived. You sat on boat and reach the other side.\nNow you started walking straight and reached a Mansion. Please decide do you want to enter it or not.\nType:- 'yes' to enter or 'no' to not enter the mansion.\t").lower()
        if decision_l2 == 'yes':
            decision_l3 = input("You came inside and saw three doors of different colours RED, BLUE and YELLOW.\nWhich door you wanna enter?(Available options are:- red, blue or yellow)\t").lower()
            if decision_l3 == 'red':
                print('As you entered room, Door closed and disappered.\nRoom started to fill with lava and you died a painful death.\nGAME OVER!')
            elif decision_l3 == 'blue':
                print('As you entered room, Door closed and disappered.\nRoom Temperature started to decrease and you died a slow death.\nGAME OVER!')
            elif decision_l3 == 'yellow':
                print("As you entered room, Door closed and disappered.\nYou got teleported to a treasure vault. All treasure in this place belongs to you.\n You found treasure. YOU WON.\n\nSURPRISE! YOU CAN NEVER EXIT THIS PLACE. YOU DIED AFTER FEW WEEKS. HAHAHAHAHA")
            else:
                print('Invalid Input.\nGAME OVER!')
        elif decision_l2 == 'no':
            print('As you tried to make distance between you and mansion. Something came and killed you.\nGAME OVER!')
        else:
            print('Invalid Input.\nGAME OVER!')
    else:
        print('Invalid input.\nGAME OVER!')