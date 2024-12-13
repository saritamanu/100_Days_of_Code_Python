# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


want_to_play = True

bid_dictionary = {}

while want_to_play:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    print("\n" * 20)
    bid_dictionary[name] = bid
    if len(bid_dictionary) >= 2:
        want_to_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
        if want_to_continue == 'no':
            smallestKey = max([[bid_dictionary[key], key] for key in bid_dictionary])
            want_to_play = False
            print(f"The winner is {smallestKey[1]} with a bid of ${smallestKey[0]}")
        else:
            want_to_play = True
