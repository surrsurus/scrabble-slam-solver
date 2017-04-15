from src.settings import *
from src import card

import random
import os

################################################################################

# Dict exception message
dict_except = "Dictionary path: '" + DICT_PATH + "' could not be found. \
Run your program from the correct directory \
or make sure to specify a path in settings.py"

# Load a dictionary
def loadDict():
    dictionary = []

    # Ensure dict exists
    if os.path.isfile(DICT_PATH):
        with open(DICT_PATH) as f:
            for line in f:
                dictionary.append(line.rstrip())

        return dictionary
    else:
        raise Exception(dict_except)

################################################################################

# Turn the alphabet string into a list
alpha = list(ALPHA)

# Create a random deck of cards
def buildDeck():
    deck = []

    for _ in range(MAX_CARDS):

        # No card can have the same front and back face, if allowed
        front, back = random.choice(alpha), random.choice(alpha)
        if not ALLOW_FACE_DUPES:
            while front == back:
                front, back = random.choice(alpha), random.choice(alpha)

        deck.append(card.Card(front, back))

    return deck

################################################################################

# Print the table of cards
def printTable(deck):
    i = 0
    for card in deck:
        i += 1
        # Insert newline once table row gets long enough
        if i % TABLE_WIDTH == 0:
            i = 0
            print(card.front + ":" + card.back + " ")
        else:
            print(card.front + ":" + card.back + " ", end='')


################################################################################

def getLongestWord(deck, dictionary):
    longestWord = ""

    for word in dictionary:
        tempDeck = [card for card in deck]
        failed = False

        # Flat out ignore words that aren't longer than the one we've previously
        # found
        if len(word) > len(longestWord):
            # Not the most optimized solution as it could potentially waste a card
            # that has a useful front or back face
            for char in list(word):
                # Search for cards that share a front face with the char
                if any(card.front.lower() == char for card in tempDeck):
                    # Remove the first instance of a card with a same front as the char
                    tempDeck.remove([card for card in tempDeck if card.front.lower() == char][0])
                # Search for cards that share a back face with the char
                elif any(card.back.lower() == char for card in tempDeck):
                    # Remove the first instance of a card with a same back as the char
                    tempDeck.remove([card for card in tempDeck if card.back.lower() == char][0])
                # Word can't be made
                else:
                    failed = True
                    break

            # Set the new longest word if found
            if failed == False:
                longestWord = word

    return longestWord

################################################################################
