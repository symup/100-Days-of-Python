BLIND AUCTION

from replit import clear
#HINT: You can call clear() to clear the output in the console.

#1.Show ASCII logo
from art import logo
print(logo)

print("Welcome to the secret auction program.")

#4.Add name and bid into dictionary as key and value
bids = {}
#5.Ask if there are other users who want to bid: create WHILE loop 
bidding_finished = False

#6. To find highest price: create function called find_highest_bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    #loop through dict
    #bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
    #2.Ask for Name input
    name = input("What is yout name?: ")
    #3.Ask for Bid price
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no.'\n")

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

   
OUTPUT:
'''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\

Welcome to the secret auction program.
What is yout name?: Angela
What's your bid?: $123
Are there any other bidders? Type 'yes' or 'no.'
no
The winner is Angela with a bid of $123.
'''

