"""
Rock paper scissors
"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

output_in_order = [rock, paper, scissors]

user_choice = int(input("Enter your choice. '0' for rock, '1' for paper, '2' for scissors.\t"))
if user_choice > 2 or user_choice < 0:
    print("invalid choice. You lose")
    exit()
print(output_in_order[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer's choice:\n{output_in_order[computer_choice]}")

if user_choice == 2 and computer_choice == 0:
    print("You lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You win.")
elif user_choice > computer_choice:
    print("You win.")
elif user_choice < computer_choice:
    print("You lose.")
else:
    print("It's a draw.")