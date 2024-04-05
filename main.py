
import random
from collections import namedtuple

# Define card suits and values (assuming single deck)
suits = ("Spades", "Hearts", "Diamonds", "Clubs")
values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
card_value = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

# Function to create a deck of cards
def create_deck():
  deck = []
  for suit in suits:
    for value in values:
      deck.append(f"{suit} {value}")
  return deck

# Function to shuffle the deck
def shuffle_deck(deck):
  random.shuffle(deck)

# Function to deal a card
def deal_card(hand, deck):
  card = deck.pop()
  hand.append(card)

# Function to calculate the value of a hand
def get_hand_value(hand):
  total = 0
  for card in hand:
    value = card_value[card.split()[1]]
    total += value
    # Handle Ace values
    if total > 21 and "A" in card:
      total -= 10
  return total

# Function to display a hand (optional)
def display_hand(hand):
  print("Hand:", hand)

# Function to check for a natural blackjack (21 with two cards)
def has_blackjack(hand):
  return len(hand) == 2 and get_hand_value(hand) == 21

# Function to check if a player or dealer should hit (get another card)
def should_hit(hand_value, dealer_value):
  return hand_value < 17 or (hand_value == 16 and dealer_value >= 7)  # Simple strategy

# Game loop
def play_blackjack():
  # Create and shuffle deck
  deck = create_deck()
  shuffle_deck(deck)

  # Deal initial cards
  player_hand = []
  dealer_hand = []
  for _ in range(2):
    deal_card(player_hand, deck)
    deal_card(dealer_hand, deck)

  # Game loop
  player_turn = True
  while player_turn or get_hand_value(dealer_hand) < 17:
    # Player turn
    if player_turn:
      display_hand(player_hand)
      total = get_hand_value(player_hand)
      print(f"Your total is: {total}")
      display_hand(dealer_hand)
      print(f"Dealer's total is: {get_hand_value(dealer_hand)}")
      choice = input("Would you like to [H]it or [S]tand? ").lower()
      if choice == 'h':
        deal_card(player_hand, deck)
      else:
        player_turn = False

    # Dealer turn (automatic)
    if not player_turn:
      dealer_total = get_hand_value(dealer_hand)
      while should_hit(dealer_total, get_hand_value(player_hand)):
        deal_card(dealer_hand, deck)
        dealer_total = get_hand_value(dealer_hand)

    # Check for bust
    if get_hand_value(player_hand) > 21 or get_hand_value(dealer_hand) > 21:
      break

  # Determine winner (if no bust)
  player_total = get_hand_value(player_hand)
  dealer_total = get_hand_value(dealer_hand)
  if has_blackjack(player_hand) and not has_blackjack(dealer_hand):
    print("Blackjack! You win!")
    print(f"\nYou have {player_hand} for a total of {player_total} and the Dealer has {dealer_hand} for a total of {dealer_total}")
  elif has_blackjack(dealer_hand) and not has_blackjack(player_hand):
    print("Blackjack! Dealer wins!")
    print(f"\nYou have {player_hand} for a total of {player_total} and the Dealer has {dealer_hand} for a total of {dealer_total}")
  elif player_total > 21:
      print("You bust! Dealer wins!")
      print(f"\nYou have {player_hand} for a total of {player_total} and the Dealer has {dealer_hand} for a total of {dealer_total}")  
  elif dealer_total > 21:
    print("Dealer bust! You win!")
    print(f"\nYou have {player_hand} for a total of {player_total} and the Dealer has {dealer_hand} for a total of {dealer_total}")
  elif player_total < dealer_total:
    print("You win!")
    print(f"\nYou have {player_hand} for a total of {player_total} and the Dealer has {dealer_hand} for a total of {dealer_total}")
  elif player_total == dealer_total:
    print("Push!")


# Start the game
play_blackjack()
