import random
from termcolor import colored

class Cards:
    """
this Cards class creates the cards and represent it
    """
# All types of suits
    card_Suits = ['Hearts', 'Diamonds', 'Clubs', 'Speads']
# All types of values
    card_Values = ['Ace', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, value, suit):
        ''' initialize the Card class values '''
        if value not in self.card_Values:
            print("wrong value")
            raise ValueError
        elif suit not in self.card_Suits:
            print('wrong suit')
            raise ValueError
        self.suit = suit
        self.value = value

    def __repr__(self):
        """
        represent the Card class
        :return:
        """
        return f'you choose {self.value} of {self.suit}'


# testing Card class
new = Cards('10', 'Diamonds')


print(new.__doc__)

"create a doc for the class and it's functions"


class Deck(Cards):

    def __init__(self):
        self._total_cards = [
            f'{x} of {i}' for x in self.card_Values for i in self.card_Suits]
        self.cards = self._total_cards.copy()

    def count(self):
        # how many cards in the deck
        return len(self.cards)

    def __repr__(self):
        # tell the user how many cards left in his deck of cards
        return f'you have a deck of {len(self.cards)} card'

    def check_cards(self):
        if not self.cards:
            print("you are out of cards ")
            raise ValueError

    def _deal(self, num):
        # it accept a number of cards to deal
        self.check_cards()
        if int(num) > len(self.cards):
            new_list = [self.cards.pop() for s in range(len(self.cards))]
        else:
            new_list = [self.cards.pop() for s in range(int(num))]
        '''for s in range(num):
            s=self.cards.pop()
            new_list.append(s) '''
        return new_list

    def shuffle(self):
        if len(self.cards) != 52:
            print(colored('           error             ',
                          color='blue', on_color='on_cyan'))
            print(colored("only full deck can be shuffed",
                          color='blue', on_color='on_cyan'))
            #raise ValueError
        else:
            return random.shuffle(self.cards)

    def deal_card(self):
        self.check_cards()
        return self.cards.pop()

    def deal_hand(self, num_of_cards):
        return self._deal(num_of_cards)

    def print_cards(self):
        for i in self.cards:
            print(i)


def new_user():
    '''
    this function deals with any regular user using Deck class
    As Follows :
    welcome to my (card/deck) app ^~^:

    here is the rules :

    r : rules
    s : shuffle
    a : show all cards in the deck
    c : deal card
    h : deal hand
    n : how many cards left

    remember the keys for each instruction
    or you can press  r  for rules

    press r for rules or e to end game
    :return:
    '''
    
    new_user = Deck()
    print('\n', colored("welcome to my (card/deck) app ^~^:",
                        color='blue', on_color='on_yellow'))
    print('\n', colored('here is the rules : ',
                        color='yellow', on_color='on_magenta'))
    rules = '\n r : rules \n s : shuffle \n a : show all cards in the deck' \
        '\n c : deal card \n h : deal hand \n n : how many cards left\n'
    print(rules, '\n', colored('remember the keys for '
                               'each instruction ', color='yellow', on_color='on_magenta'), '\n',
          colored('or you can press  r  for rules', color='red', on_color='on_cyan'))
    while True:
        decision = input('\npress r for rules or e to end game\n').lower()
        if decision == 'e':
            break
        elif decision == 'r':
            print(rules)
        elif decision == 's':
            new_user.shuffle()
            print("the cards has been shuffled ")
        elif decision == 'a':
            print("\n", colored('here is the remaining cards :',
                                color='green', on_color='on_yellow'), "\n")
            new_user.print_cards()
            print('\n', colored(f'these were all {new_user.count()} cards',
                                color='yellow', on_color='on_green'), '\n')
        elif decision == 'c':
            dealt = new_user.deal_card()
            print(f'you dealt a ({dealt})')
        elif decision == 'h':
            try:
                num = input(
                    "how many cards you want to delete ? \nNOTE : only numbers allowed\n")
                hand = new_user.deal_hand(num)
                print(f'you dealt {num} :')
                for card in hand:
                    print(card)
            except:
                print('you enter a wrong input ')
                print(colored('i said only numbers allowed',
                              color='red', on_color='on_yellow'))
        elif decision == 'n':
            print(new_user)
        else:
            print(colored('      wrong input       '.upper(),
                          color='blue', on_color='on_red'))
            print(colored('please follow the rules ',
                          color='blue', on_color='on_red'))

new_user()
