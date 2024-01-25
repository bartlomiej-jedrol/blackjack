import random
import os
from art import logo

def deal_card():
    """Return a random card from a deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    """Calculate the score for a given hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def compare(user_score, computer_score):
    """Compare user's and computer's scores."""
    if user_score > 21 and computer_score > 21:
        print("     You went over. You lose :(.\n")
    elif user_score == computer_score:
        print("     Draw.\n")
    elif computer_score == 0:
        print("     Computer has blackjack, you lose :(.\n")
    elif user_score == 0:
        print("     You have blackjack! You win :).\n")
    elif computer_score > 21:
        print("     Computer went over. You win :).\n")
    elif user_score > 21:
        print("     You went over. You lose :(.\n")
    elif user_score > computer_score:
        print("     You have a higher score. You win :).\n")
    elif user_score < computer_score:
        print("     You have a lower score. You lose :(.\n")

def play_game():
    """Play a blackjack game."""
    print(logo)
    user_hand = []
    computer_hand = []
    # Deal starting hands.
    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"     Your cards: {user_hand}, your score: {user_score}.")
    print(f"     Computer cards: [{computer_hand[0]} X].\n")

    # Check if user or computer does not have a blackjack.
    if user_score != 0 and computer_score != 0:
        # Deal card for for the user based on its choice and if the score does not exceed 21.
        while user_score < 21 and input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
            user_hand.append(deal_card())
            user_score = calculate_score(user_hand)
            print(f"     Your cards: {user_hand}, your score: {user_score}.")
            print(f"     Computer cards: {computer_hand[0]} X].\n")
                
    while user_score < 21 and computer_score < 17:
        # Deal card for the computer until the score goes over 16.
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
        print(f"     Your cards: {user_hand}, your score: {user_score}.")
        print(f"     Computer cards: {computer_hand}, computer score: {computer_score}.\n")

    print(f"     Your final cards: {user_hand}, your final score: {user_score}.")
    print(f"     Computer final cards: {computer_hand}, computer final score: {computer_score}.\n")

    compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system("clear")
    play_game()
