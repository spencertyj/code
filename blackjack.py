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
        print ('[' + self.rank + 'of' + self.suit + ']' )
def new_deck():
    deck = []
    suits = ['\u2664','\u2661','\u2667','\u2662']
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    for i in suits:
        for r, v in zip(ranks, values):
            deck.append(card(i,r,v))
    return deck
def cal_value(hand):
   value = 0
   for i in hand:
     value = i.value + value
   return value
def cal_value(hand):
    for c in hand:
        total += c.value
        if c.rank == 'A':
            aces += 1
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

deck = []
player = []
dealer = []
deck.extend(new_deck())
deck.extend(new_deck())
deck.extend(new_deck())
random.shuffle(deck)
temp = deck.pop()
player.append(temp)
temp = deck.pop()
player.append(temp)
temp = deck.pop()
dealer.append(temp)
temp = deck.pop()
temp.facedown = True
dealer.append(temp)
print("Dealer:")
display_cards(dealer)
while True:
  print("player")
  display_cards(player)
  choice = input("Hit (H) for another card, Stand (S) to stop.")
  if choice == "H":
    temp = deck.pop()
    player.append(temp)
    continue
  elif choice == "S":
    print("End of turn.")
    break
print("Player's Deck")
display_cards(player)
player_value = cal_value(player)
print ("Player's Deck Value:")
print (player_value)
print("\nDealer's Deck (reveal):")
dealer[1].facedown = False
display_cards(dealer)
dealer_value = cal_value(dealer)
print ("Dealer's Deck value:")
print (dealer_value)
while cal_value(dealer) < 17:
    print("Dealer hits.")
    dealer.append(deck.pop())
    display_cards(dealer)
    dealer_value = cal_value(dealer)
    print("Dealer's Deck value:", dealer_value)
    if dealer_value > 21:
        print("Dealer Busted")
        break
if cal_value(dealer) >= 17 and cal_value(dealer) <= 21:
    print("Dealer stands with value:", cal_value(dealer))
    print("Final Results:")
print("Player:", cal_value(player))
print("Dealer:", cal_value(dealer))
if cal_value(player) > 21:
    print("Player busted — dealer wins.")
elif cal_value(dealer) > 21:
    print("Dealer busted — player wins.")
elif cal_value(player) > cal_value(dealer):
    print("Player wins.")
elif cal_value(player) < cal_value(dealer):
    print("Dealer wins.")
else:
    print("Tie.")
