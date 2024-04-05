import random
playerIn = True
dealerIn = True

#deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

#deal the cards 
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#calculate the total od each hand
def total(turn):
    total = 0
    face = ['J', 'Q', 'K', 'A'] 
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        elif card == 'A':
            if total >= 11:
                total += 1
            else:
                total += card
        else:
            total += card
    return total

#check for winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
    
# game loop 
for _ in range(2):
    dealCard(playerHand)
    dealCard(dealerHand)

print("Your hand is: ", playerHand)
print("Your total is: ", total(playerHand))

print("Dealer's hand is: ", revealDealerHand())
print("Dealer's total is: ", total(dealerHand))

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")   
    print(f"Your have {playerHand} for a total of {total(playerHand)}")

    if playerIn:
        choice = input("Would you like to [H]it or [S]tand? ").lower()
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if choice == 'h':
        dealCard(playerHand)
    elif choice == 's':
        playerIn = False
    
    if total(playerHand) > 21:
        playerIn = False
    if total(dealerHand) > 21:
        dealerIn = False
if total(playerHand) == 21:
    print("Blackjack! You win!")
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the Dealer has {dealerHand} for a total of {total(dealerHand)}")
elif total(dealerHand) == 21:
    print("Blackjack! Dealer wins!")
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the Dealer has {dealerHand} for a total of {total(dealerHand)}")
elif total(playerHand) > 21:
    print("You bust! Dealer wins!")
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the Dealer has {dealerHand} for a total of {total(dealerHand)}")
elif total(dealerHand) > 21:
    print("Dealer bust! You win!")
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the Dealer has {dealerHand} for a total of {total(dealerHand)}")
elif 21 - total(playerHand) < 21 - total(dealerHand):
    print("Dealer wins!")
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the Dealer has {dealerHand} for a total of {total(dealerHand)}")
elif 21 - total(playerHand) > 21 - total(dealerHand):
    print("You win!")
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the Dealer has {dealerHand} for a total of {total(dealerHand)}")