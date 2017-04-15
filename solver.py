from src.scrabbleslam import loadDict, buildDeck, printTable, getLongestWord

# Main
if __name__ == "__main__":

    # Load up the dictionary
    dictionary = loadDict()

    # Create a deck
    deck = buildDeck()

    # Let the user see their deck
    printTable(deck)

    # Print the longest word
    print(getLongestWord(deck, dictionary))
