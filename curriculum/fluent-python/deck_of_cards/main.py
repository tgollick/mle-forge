import random

RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
SUITS = ('♠','♥','♦','♣')

# Return the deck of cards
def make_deck():
    return [(rank, suit) for suit in SUITS for rank in RANKS]

# Random shuffle the deck 
def shuffle_deck(deck):
    random.shuffle(deck)

# Draw from the deck
def draw_card(deck):
    if not deck:
        raise IndexError("Deck is empty!")
    return deck.pop()

# Deal hands from the deck
def deal_cards(deck, n_players, n_cards):
    return [[draw_card(deck) for _ in range(n_cards)] for _ in range(n_players)]

# Main function
if __name__ == "__main__":
    deck = make_deck()
    print(f"Deck length: {len(deck)}")
    shuffle_deck(deck)
    hands = deal_cards(deck, 3, 8) # Uno style baby

    for i, h in enumerate(hands, start=1):
        print(f"Player {i}:", " ".join(f"{r}{s}" for r, s in h))
