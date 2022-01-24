#Author:(Arsalan Ahmad)
#Date: 1/24/2022

class cards:
    def __init__(self):
        self.cards = []
        self.first_card = 0
        self.last_card = 0

    def set_up(self):
        self.make_and_add_cards_to_deck("spades")
        self.make_and_add_cards_to_deck("hearts")
        self.make_and_add_cards_to_deck("diamond")
        self.make_and_add_cards_to_deck("clubs")
        self.first_and_last_card()

    def make_and_add_cards_to_deck(self, color):
        cards = []
        cards.append((color, "Ace"))
        cards.append((color, "jack"))
        cards.append((color, "King"))
        cards.append((color, "Queen"))
        i = 2
        while i <= 10:
            cards.append((color, i))
            i = i + 1
        self.cards = self.cards + cards

    def print_cards(self):
        print(self.cards)

    def in_shuffle_cards(self):
        # we are going to split the deck of cards
        total_length = len(self.cards)
        half_point = int(total_length / 2)
        first_half = self.cards[:half_point]
        second_half = self.cards[half_point:]

        shuffled_version = []
        #time to ruffle shuffle
        while True:
            if len(first_half) != 0 and len(second_half) != 0:
                shuffled_version.append(first_half.pop())
                shuffled_version.append(second_half.pop())
            else:
                break
        
        self.cards = shuffled_version

    def first_and_last_card(self):
        self.first_card = self.cards[0]
        self.last_card = self.cards[-1]
    
    def position_of_first_card(self):
        return self.cards.index(self.first_card)
    
    def position_of_last_card(self):
        return self.cards.index(self.last_card)

    def first_card_becomes_bottom(self):
        if self.cards.index(self.first_card) == 51:
            return True
        else:
            return False

    def first_and_last_card_meet(self):
        if self.position_of_first_card() + 1 == self.position_of_last_card() or self.position_of_first_card() - 1 == self.position_of_last_card():
            return True
        else:
            return False


deck_1 = cards()
deck_1.set_up()

#Deck 1 will solve the 7th shuffle problem
for i in range(7):
    deck_1.in_shuffle_cards()
print("The position of first card is " + str(deck_1.position_of_first_card()))

# Time to make deck 2
deck_2 = cards()
deck_2.set_up()

# Deck 2 will solve the top card == bottom card problem
i = 0
while True:
    #check if the first card has become the bottom card
    if deck_2.first_card_becomes_bottom() == True:
        break
    else:
         deck_2.in_shuffle_cards()
    i = i + 1


print("It takes " + str(i) + " shuffles for first card to become the bottom card")


#Time to make deck_3
deck_3 = cards()
deck_3.set_up()

#Deck 3 will solve the first card touching the last card problem
j = 0
while True:
    if deck_3.first_and_last_card_meet() == True:
        break
    else:
        deck_3.in_shuffle_cards()
    j = j + 1
print("It takes " + str(j) + " shuffles for first and last card to to touch each other")
