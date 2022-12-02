import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bid_data = {}

def new_user_data(name,bid):
    bid_data[name] = bid
'''
max_bid = -1
max_bid_username = ""
'''
response = "yes"

while response == 'yes':
    #username
    bidder = input("Enter your name?\n")

    #bid amount
    amount = int(input("Enter your bid amount?\n"))

    #adding bidder and his bid amount in dictionary
    new_user_data(bidder, amount)
    '''
    #finding maximum bid
    if amount > max_bid:
        max_bid = amount
        max_bid_username = bidder
    '''
    #asking if there is another person
    response = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system('cls')

'''
print(f"The winner is {max_bid_username} with a bid of ${max_bid}.")

'''
def find_highest_bid_amount(bid_data):
    max_bid = 0
    max_bid_bidder = ""
    for bidder in bid_data:
        if bid_data[bidder] > max_bid:
            max_bid_bidder = bidder
            max_bid = bid_data[bidder]
    print(f"The winner is {max_bid_bidder} with a bid of ${max_bid}.")

find_highest_bid_amount(bid_data)
