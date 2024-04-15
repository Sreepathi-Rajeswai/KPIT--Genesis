'''class card:
    def __main__(self,s=0,r=2):
        self.s=s;self.r=r
        s_n=['clubs','diamonds','hearts','spades']
        r_n=[None,'ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
    def __str__(self) -> str:
        
        return '%s of %s'%(card.r_n[self.r],card.s_n[self.s])
    def __lt__(self,o):
        t1=self.s,self.r
        t2=o.s,o.r
        return t1<t2
class Deck:
    def __init__(self):
        self.cards=[]
        for s in range(4):
            for r in range(1,14):
                #card=card(s,r)
                self.cards.append(card)
    def __str__(self) -> str:
        res=[]
        for card in self.cards:
            res.append(str(card))
            return '\n'.join(res)
    def __pop__card(self):
        return self.cards.pop()
    def __add__card(self,card):
        self.cards.append(card)
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def sort(self):
        sorted=self.sort()
        return sorted
class Hand(Deck):
    def __init__(self,label=''):
        self.cards=[]
        self.label=label
    def move_cards(self,hand,num):
        for i in range(num):
            hand.add_card(self.pop_card())
    def deal_hands(self,num_hands,cards_per_hand):
        if num_hands*cards_per_hand>len(self.cards):
            return "not enough"
        l=[]
        for _ in range(num_hands):
            hand=Hand()
            for _ in range(cards_per_hand):
                card=self.deal_card()
                if card:
                    hand.__add__card(card)
                    hand.append(hand)
                return hand

hand=Hand('new hand')
hand.cards
deck=Deck()
#card=deck.pop_card()
#print(hand)
print(deck)'''
#2
class card:
    def __main__(self,s=0,r=2):
        self.s=s;self.r=r
        s_n=['clubs','diamonds','hearts','spades']
        r_n=[None,'ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
    def __str__(self) -> str:
        
        return '%s of %s'%(card.r_n[self.r],card.s_n[self.s])
    def __lt__(self,o):
        t1=self.s,self.r
        t2=o.s,o.r
        return t1<t2
class Deck(object):
    # Alternative with nasty list comprehension
    # self.cards = [Card(suit,rank) for suit in range(4)
    #         for rank in range(1, 14)]
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        # Or use a list comprehension
        # res = [str(card) for card in self.cards]
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def sort(self):
        # Method to have deck sort itself.
        self.cards.sort(cmp=card.__cmp__)


def main():
	pass


if __name__ == '__main__':
	main()


    