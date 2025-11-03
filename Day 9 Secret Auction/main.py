from art import logo

# Printing welcome message
print(logo)
print("Welcome to the secret auction program.")

bids = {}


# Finding the highest bidder
def find_highest_bidder(bids):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
    return highest_bidder, highest_bid


bidding_finisher = False

# APPLICATION
while not bidding_finisher:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    print(f"{name} bid ${bid}")
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no': ")
    if continue_bidding == "no":
        bidding_finisher = True
        # Find the highest bidder
        highest_bidder, highest_bid = find_highest_bidder(bids)
    else:
        print("\n" * 50)


print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}")
