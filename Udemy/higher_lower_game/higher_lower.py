#importing required modules
import random
from os import system
#importing art works and game data's ; Assigning variables to them
import art
import game_data

logo = art.logo
vs = art.vs
data = game_data.data

def info(profile):
    print(f"{profile['name']}, a {profile['description']}, from {profile['country']}.")

def game():
    print(logo)
    score = 0
    response = True
    while response:
        selected_profiles = random.sample(data, 2)
        first_person_follower = selected_profiles[0]["follower_count"]
        second_person_follower = selected_profiles[1]["follower_count"]
        if first_person_follower > second_person_follower:
            expected_response = "A"
        elif second_person_follower > first_person_follower:
            expected_response = "B"
        info(selected_profiles[0])
        print(vs)
        info(selected_profiles[1])
        gusse = input("Who has more followers? Type 'A' or 'B': ").upper()
        if gusse == expected_response:
            score += 1
            system('cls')
            print(logo)
            print(f"You're right! Current score: {score}.")
        elif gusse != expected_response:
            system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            response = False

game()