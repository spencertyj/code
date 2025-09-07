import random

# Function to print the cards
def display_cards(cards):
  s = ""
  for card in cards:
    s = s + "\t ________________"
  print(s)
 
  s = ""
  for card in cards:
    s = s + "\t|                |" 
  print(s)
 
  s = ""
  for card in cards:
    if card.facedown:
      s = s + "\t|  ?             |"  
    else:
      if card.rank == '10':
        s = s + "\t|  {}            |".format(card.rank)
      else:
        s = s + "\t|  {}             |".format(card.rank)
  print(s)
 
  s = ""
  for card in cards:
      s = s + "\t|                |"
  print(s)    
 
  s = ""
  for card in cards:
    s = s + "\t|                |"
  print(s)    
 
  s = ""
  for card in cards:
    s = s + "\t|                |"
  print(s)    
 
  s = ""
  for card in cards:
    s = s + "\t|                |"
  print(s)    
 
  s = ""
  for card in cards:
    if card.facedown:
      s = s + "\t|       ?        |"
    else:
      s = s + "\t|       {}        |".format(card.suit)
  print(s)    
 
  s = ""
  for card in cards:
    s = s + "\t|                |"
  print(s)    
 
  s = ""
  for card in cards:
    s = s + "\t|                |"
  print(s)
 
  s = ""
  for card in cards:
    s = s + "\t|                |"
  print(s)
 
  s = ""
  for card in cards:
    s = s + "\t|                |"
  print(s)    
 
  s = ""
  for card in cards:
    if card.facedown:
      s = s + "\t|             ?  |"  
    else:
      if card.rank == '10':
        s = s + "\t|            {}  |".format(card.rank)
      else:
        s = s + "\t|            {}   |".format(card.rank)
  print(s)
         
  s = ""
  for card in cards:
    s = s + "\t|________________|"
  print(s)        
 
  print()

class card:
    def __init__(self, suit, rank, value):
        # Suit of the card like spades and clubs
        self.suit = suit
        # Represent value of the card like A for ace, K for king
        self.rank = rank
        # Score value for the card like 10 for king
        self.value = value
        self.facedown = False

    def print_card(self):
        print ('[' + self.rank + 'of' + self.suit + ']')

def new_deck():
    deck = []
    suits = ['\u2664','\u2661','\u2667','\u2662']#Spades, Hearts, Clubs and Diamonds
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    for i in suits:
        for r, v in zip(ranks, values):
            deck.append(card(i,r,v))
    return deck

#main
deck = []
deck.extend(new_deck())
deck.extend(new_deck())
deck.extend(new_deck())
random.shuffle(deck)
print(len(deck))
deck.pop().print_card()
deck.pop().print_card()
print(len(deck))
print(len(deck))
display_cards([deck.pop(),deck.pop()])
print(len(deck))
mycard = deck.pop()
mycard.facedown = True
display_cards([mycard])
