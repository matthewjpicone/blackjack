# Blackjack

Welcome to the Simple Blackjack Game! This is a Python implementation of the classic casino game using the Tkinter module for the graphical user interface. 

## Game Components

The game creates a main window and a card frame. The user plays against the computer. The following are the main functions and components of the game:

- The `play()` function is the main function of the program. It calls the `new_game()` function to start a new game.
- The `new_game()` function creates the game's components, such as the cards, the scores, and the result text. It also resets the game state, such as the dealer and player hands, and the deck of cards.
- The `load_images()` function loads all the card images from a local directory into a list called `card_images`.
- The `deal_card()` function pops the next card from the deck, appends it to the dealer or player's hand, and displays the card on the GUI.
- The `score_hand()` function calculates the score for a given hand of cards.
- The `deal_dealer()` function handles the dealer logic, such as hitting and standing. The dealer will hit until they reach a score of 17 or higher or until their score is higher than the player's score. If the dealer busts or has a lower score than the player, the player wins. If the dealer has a higher score than the player, the dealer wins.
- The `deal_player()` function handles the player's turn. When the player clicks the "Hit" button, the function adds a card to the player's hand and calculates the new score. If the player's score is greater than 21, the dealer wins. If the player's score is 21 or less, the `deal_dealer()` function is called.
- The `tally` dictionary keeps track of the number of games won by the player, computer, and draws.

## Credits

Credit to David Bellot for creating the card images used in the game. Check out his work at http://svg-cards.sourceforge.net/.

## How to Play

To start the game, simply run the `blackjack.py` file. The game will open in a new window. Click the "Hit" button to draw a new card from the deck. Click the "New Game" button to start a new game. The goal of the game is to get a higher score than the dealer without going over 21. If you go over 21, you lose the game. If you get a score of 21 or less and the dealer's score is lower than yours or the dealer goes over 21, you win the game. 

## Screenshots

Here are some screenshots of the game in action:

![Game View 1](https://github.com/matthewjpicone/blackjack/blob/main/images/blackjack1.png?raw=true)

![Game View 2](https://github.com/matthewjpicone/blackjack/blob/main/images/blackjack2.png?raw=true)

![Game View 3](https://github.com/matthewjpicone/blackjack/blob/main/images/blackjack3.png?raw=true)
