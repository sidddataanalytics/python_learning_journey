print("Welcome to the blind auction!")
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue.lower() == "no":
        bidding_finished = True
        highest_bidder = ""
        highest_bid = 0
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                highest_bidder = bidder
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")  
        
print(bids)
        