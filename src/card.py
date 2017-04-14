class Card(object):
    """Card objects holds the front and back of a card"""
    def __init__(self, front, back):
        super(Card, self).__init__()

        self.front = front
        self.back = back
