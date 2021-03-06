import random

#generate a card deck
card_deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def poker(hands):
    "Return the best hand: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    key = key or (lambda x: x)
    max_list = []
    max_val  = None
    for i in iterable:
        val = key(i)
        if not max_val or val > max_val:
            max_list = [i]
            max_val = val
        elif max_val == val:
            max_list.append(i)
    return max_list

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks),ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks),ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks),ranks)
    else:                                          # high card
        return  (0,ranks)

def card_ranks(cards):
    def card_value(card):
        """ card_value: Return card value from 2 to 14 """
        if card == 'T':
            return 10
        if card == 'J':
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13
        elif card == 'A':
            return 14
        return int(card)
    "Return a list of the ranks, sorted with higher first."
    ranks = [card_value(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    current_card = ranks[0]
    for card in ranks[1:]:
        if card != current_card-1:
            return False
        current_card = card
    return True

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return all(x == suits[0] for x in suits)

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    freq = {}
    for card in ranks:
        if card in freq:
            freq[card] += 1
        else:
            freq[card] = 1
    for card in ranks:
        if freq[card] == n:
            return card
    return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    prev  = None
    pairs = ()
    for card in ranks:
        if card == prev:
            pairs += (card,)
            prev = None
        else:
            prev = card
    if len(pairs) == 2 and len(set(pairs))==2:
        return pairs
    return None

def deal(numhands, n=5, deck=card_deck):
    """Shuffle a deck and return hands.
       in case there is not enough card return None"""
    if n*numhands > len(deck):
        return None
    random.shuffle(deck)
    hands = []
    for hand in range(numhands):
        hands.append(deck[hand*n:hand*n+n])
    return hands

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert card_ranks(sf) == [10,9,8,7,6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'

def test_hands():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'

def test_kind():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'

def test_pairs():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert two_pair(tpranks) == (9,5)
    return 'tests pass'
# test()
# print(card_ranks(['AC', '3D', '4S', 'KH'])) #should output [14, 13, 4, 3]
print(test_hands())
print(test_kind())
print(test_pairs())
print(str(allmax([1,2,3,5,5,4,1])))
print(str(deal(3)))
