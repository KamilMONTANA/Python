import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "K", "Q", "J"]
player = []
dealer = []


def calculate_score(hand):
    """Calculate the total score of a hand, handling Aces as 1 or 11."""
    total = 0
    aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            aces += 1
            total += 11
        else:
            total += card
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def check_bust(player_score, dealer_score):
    """Check if either player or dealer has busted (score > 21)."""
    if player_score > 21:
        return "Dealer wins!"
    elif dealer_score > 21:
        return "Player wins!"
    return "Game continues..."


def dealer_hit(dealer):
    """Have the dealer hit until their score is at least 17."""
    while calculate_score(dealer) < 17:
        dealer.append(random.choice(deck))
    return dealer


def show_result(player_score, dealer_score):
    """Determine the result of the game based on scores."""
    if player_score > dealer_score:
        return "Player wins!"
    elif dealer_score > player_score:
        return "Dealer wins!"
    return "It's a tie!"


def playerDeck():
    """Deal 2 cards to player."""
    player.clear()
    for _ in range(2):
        player.append(random.choice(deck))
    return player


def dealerDeck():
    """Deal 2 cards to dealer (one hidden)."""
    dealer.clear()
    for _ in range(2):
        dealer.append(random.choice(deck))
    return dealer


def choice():
    """Player can choose to hit or stand."""
    print("Choose option:")
    print("1. Hit")
    print("2. Stand")
    option = int(input("Option: "))
    return option


def hit():
    """If player chooses to hit, deal 1 card."""
    player.append(random.choice(deck))
    return player


def stand():
    """Player stands, end of player's turn"""
    return dealer


while True:
    print("-------BLACKJACK-------")
    playerDeck()
    dealerDeck()

    # Show player's hand and one dealer card
    print(f"Player: {player}")
    print(f"Dealer: [{dealer[0]}, ?]")

    # Player's turn
    while True:
        option = choice()
        if option == 1:
            hit()
            print(f"Player: {player}")
            if calculate_score(player) > 21:
                print("Player busts! Dealer wins.")
                break
        elif option == 2:
            stand()
            break
        else:
            print("Invalid option")
            continue

    # If player didn't bust, dealer's turn
    if calculate_score(player) <= 21:
        dealer_hit(dealer)
        print(f"Dealer: {dealer}")
        dealer_score = calculate_score(dealer)
        if dealer_score > 21:
            print("Dealer busts! Player wins.")
        else:
            player_score = calculate_score(player)
            result = show_result(player_score, dealer_score)
            print(result)

    # Ask to play again
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
