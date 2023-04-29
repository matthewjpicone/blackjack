# !/usr/bin/env python3
"""
    29/10/2022 04:12 pm
    Author: matthewpicone

    Project: blackjack
    blackjack.py.py  - This is a simple implementation of the Black Jack game
    in Python.

    
    See readme.md for details. 
    
    """


# Test for python version
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import random


def play():
    __name__ = '__main__'


def load_images(card_images):
    """
    Loads all card images from a local directory into a list.

    Args:
    - card_images: A list to store the card images.

    Returns:
    - None.

    The function iterates through each card in a deck of playing cards, creates
    a PhotoImage object for each card, and appends a tuple of the card's value
    and its PhotoImage object to the card_images list. The cards are stored in
    PNG format if the version of Tkinter is 8.6 or later, and in PPM format
    otherwise.

    Example usage:
    card_images = []
    load_images(card_images)
    """

    suits = ['heart', 'diamond', 'club', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    """
    Deals a card from the deck and displays it on the given frame.
    
    Args:
    - frame: a tkinter Frame object to display the card image on.
    
    Returns:
    - A tuple representing the dealt card, consisting of:
        * The card's face value (an integer between 1 and 10)
        * A tkinter PhotoImage object containing the card's image.
    
    The function pops the next card from the deck list, appends it back to the
    end of the list, and creates a Label widget with the card's image on the
    given frame, before returning the dealt card's tuple.
    """
    # Deals a card
    # pop next card from deck
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    """
    Calculates the score of the given hand for the player.

    Parameters:
    hand (list): A list of tuples representing the cards in the hand. Each
    tuple contains the value and image of the card.

    Returns:
    int: The score of the hand.

    """
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    """
    Handles the dealer logic by drawing cards from the deck until the dealer
    has a score greater than or equal to 17, or until their score is greater
    than the player's score. Once the dealer is finished drawing cards, the
    function determines the winner of the game and updates the result_text
    label accordingly.

    Args:
    None.

    Returns:
    None.
    """

    dealer_score = score_hand(dealer_hand)
    player_score = score_hand(player_hand)
    while 0 < dealer_score < 17 and dealer_score < player_score:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)

    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
    else:
        result_text.set("Draw")


def deal_player():
    """
    Deals a card to the player, updates the player's score, and calls the
    deal_dealer function. If the player's score is greater than 21, sets the
    result_text variable to "Dealer Wins!".

    Parameters:
    - None

    Returns:
    - None
    """

    # Append the card to the player's hand
    player_hand.append(deal_card(player_card_frame))

    # Update the player's score and display it
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)

    # Call deal_dealer function to update dealer's hand and score
    deal_dealer()

    # If player's score is greater than 21, set result_text to "Dealer Wins!"
    if player_score > 21:
        result_text.set("Dealer Wins!")


def new_game():
    """
    Resets the game for a new round.

    Global variables:
    dealer_card_frame (tkinter.Frame): The frame displaying the dealer's cards.
    player_card_frame (tkinter.Frame): The frame displaying the player's cards.
    dealer_hand (list): The list of cards in the dealer's hand.
    player_hand (list): The list of cards in the player's hand.
    deck (list): The list of cards in the deck.
    first_game (bool): Indicates whether it is the first round of the game.
    result_tally_str (tkinter.StringVar): The string variable storing the
    result tally string.
    result_tally (dict): The dictionary storing the result tally.

    Returns:
    None.
    """

    global dealer_card_frame, player_card_frame, dealer_hand, player_hand, \
        deck, first_game, result_tally_str, result_tally
    # Update result tally if it's not the first game
    if first_game:
        first_game = False
    else:
        dealer_score = score_hand(dealer_hand)
        player_score = score_hand(player_hand)
        if (dealer_score < player_score or dealer_score > 21) and (
                player_score <= 21):
            tally['Player'] += 1
        elif (player_score < dealer_score or player_score > 21) and (
                dealer_score <= 21):
            tally['Computer'] += 1
        elif dealer_score == player_score and player_score <= 21:
            tally['Draw'] += 1
        result = ''
        for key, val in tally.items():
            result += key + ": " + str(val) + "  "
        result_tally_str.set(result)

    # Reset the card frames, hands, and result text
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    dealer_hand = []
    player_hand = []
    result_text.set("")

    # Shuffle the deck and deal the cards
    random.shuffle(deck)
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

    print(deck)


def play():
    """
    Starts a new game of Blackjack and runs the game window.
    """
    new_game()
    mainwindow.mainloop()


# Set the initial values for the game
first_game = True
tally = {'Player': 0, 'Computer': 0, 'Draw': 0}

# Create the main window for the game
mainwindow = tkinter.Tk()
mainwindow.title("Black Jack")
mainwindow.geometry("640x480")
mainwindow.configure(backgroun='green')

# Create a label for displaying the result of the game
result_text = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
result.configure(background='green', fg='white')

# Create a frame for displaying the dealer's cards
card_frame = tkinter.Frame(mainwindow, relief="sunken", borderwidth=1,
                           background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# Create a label for displaying the dealer's score
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green",
              fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label,
              background="green", fg="white").grid(row=1, column=0)

# Create a frame for displaying the dealer's cards
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

# Create a label for displaying the player's score
player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green",
              fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label,
              background="green", fg="white").grid(row=3, column=0)

# Create a frame for displaying the player's cards
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Create a frame for the game buttons
button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row=3, column=0, sticky='w')

# Create a button for the player to "hit"
player_button = tkinter.Button(button_frame, text='Hit me!',
                               command=deal_player)
player_button.grid(row=0, column=0)

# Create a button to start a new game
new_game_button = tkinter.Button(button_frame, text='New Game',
                                 command=new_game)
new_game_button.grid(row=0, column=1)

# Create a label for displaying the game's results tally
result_tally_str = tkinter.StringVar()
result_tally = tkinter.Label(mainwindow, textvariable=result_tally_str)
result_tally.grid(row=4, column=0, columnspan=2, sticky='w')
result_tally.configure(background='green', fg='white')

# Load the images of the cards and create a new deck of shuffled cards
cards = []
load_images(cards)
deck = list(cards)

# Initialize the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()
