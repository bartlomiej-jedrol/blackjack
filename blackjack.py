import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Returns a random card from a range of cards list.
def return_random_card():
    card_index = random.randint(0, len(cards)-1)
    return cards[card_index]

# Returns the starting hand containing two cards.
def deal_starting_hand():
    starting_hand = []
    for _ in range(2):
        starting_hand.append(return_random_card())
    return starting_hand

# Calculates score for a given hand.
def calculate_score(hand):
    score = 0
    has_ace = False

    for card in hand:
        score += card
        if card == 11:
            has_ace = True
            ace_index = hand.index(card)
        
    # Calculates aces as 1 if the score exceeds 21.
    if score > 21 and has_ace:
        hand[ace_index] = 1
        score = 0
        for card in hand:
            score += card
    
    return score

# Prints a hand and a score of a user and first card and score of a computer.
def print_unrevealed(user_hand, computer_hand, user_score):
    print(f"     Your cards: {user_hand}, your score: {user_score}.")
    print(f"     Computer cards: [{computer_hand[0]} X], computer score: {computer_hand[0]}.\n")

# Prints a hand and a score of a user and a computer.
def print_revealed(user_hand, computer_hand, user_score, computer_score):
    print(f"     Your cards: {user_hand}, your score: {user_score}.")
    print(f"     Computer cards: {computer_hand}, computer score: {computer_score}.\n")

# Prints a final hand and a final score of a user and a computer.
def print_final(user_hand, computer_hand, user_score, computer_score):
    print(f"     Your final cards: {user_hand}, your final score: {user_score}.")
    print(f"     Computer's final cards: {computer_hand}, computer's final score: {computer_score}.\n")

# Evaluates user decision on the another card.    
def want_card():
    want_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if want_card == "y":
        another_card = True
    elif want_card == "n":
        another_card = False
    return another_card

# Evaluates user decision on the another game.
def want_continue():
    want_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_continue == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        blackjack()
    elif want_continue == "n":
        exit()

# Runs the blackjack game.
def blackjack():
    user_hand = deal_starting_hand()
    computer_hand = deal_starting_hand()
    
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    if computer_score == 21:
        print_revealed(user_hand, computer_hand, user_score, computer_score)
        print("     Computer has blackjack, you lose :(.")
        want_continue()
    elif user_score == 21:
        print_revealed(user_hand, computer_hand, user_score, computer_score)
        print("     You have blackjack! You win :).")
        want_continue()
    else:
        print_unrevealed(user_hand, computer_hand, user_score)
    
    another_card = want_card()
    while another_card == True:
        user_hand.append(return_random_card())
        user_score = calculate_score(user_hand)
        if user_score == 21:
            print_revealed(user_hand, computer_hand, user_score, computer_score)
            print("     You have blackjack! You win :).\n")
            want_continue()
        elif user_score > 21:
            print_revealed(user_hand, computer_hand, user_score, computer_score)
            print("     You went over. You lose :(.\n")
            want_continue()
        else:
            print_unrevealed(user_hand, computer_hand, user_score)
        
        another_card = want_card()

    # Prints initial computer's hand.
    print_revealed(user_hand, computer_hand, user_score, computer_score)

    while computer_score <= 16:
        computer_hand.append(return_random_card())
        computer_score = calculate_score(computer_hand)
        if computer_score == 21:
            print_revealed(user_hand, computer_hand, user_score, computer_score)
            print("     Computer has blackjack, you lose :(.\n")
            want_continue()
        elif computer_score > 21:
            print_revealed(user_hand, computer_hand, user_score, computer_score)
            print("     Computer went over. You win :).\n")
            want_continue()
        # Prints each hand that the computer gets.
        elif computer_score <= 16:
            print_revealed(user_hand, computer_hand, user_score, computer_score)
    
    if user_score > computer_score:
        print_final(user_hand, computer_hand, user_score, computer_score)
        print("     You have a higher score. You win :).\n")
    elif user_score < computer_score:
        print_final(user_hand, computer_hand, user_score, computer_score)
        print("     You have a lower score. You lose :(.\n")
    elif user_score == computer_score:
        print_final(user_hand, computer_hand, user_score, computer_score)
        print("     It's a draw.\n")

    want_continue()
        
blackjack()
