import random

def result(player_cards, computer_cards):
    player_cards_sum = sum(player_cards)
    computer_card_sum = sum(computer_cards)
    if player_cards_sum > 21:
        print("You lose. You went over 21.")
    elif computer_cards_sum > 21:
        print("You win. Computer went over 21.")
    elif player_cards_sum == computer_card_sum:
        print("You draw.")
    elif player_cards_sum > computer_card_sum:
        print("Win with a Blackjack.")
    else:
        print("You lose. Computer has Blackjack")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []

# choosing players card
player_cards.append(random.choice(cards))
player_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))

print(player_cards)
print(computer_cards[0])

response = input("Do you want draw a new card. Type 'y' for drawing new card and 'n' for getting result for present cards.")
if
