import unittest
from answer_of_deck_card_app_ex import *

'to test errors you need with statment'

class MyTestCase(unittest.TestCase):

    def test_class_card(self):
        modi=Card('modi', 'the sea')
        self.assertEqual(modi.__repr__(), "modi of the sea" )
        
    def setUp(self):
        self.deck_object =Deck()
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [f'{value} of {suit}' for suit in suits for value in values]
        
    def test_repr(self):
        self.assertEqual(self.deck_object.__repr__(),'Deck of 52 cards')
        
    def test_count(self):
        self.assertEqual(self.deck_object.count(),52)
        
    def test_deal(self):
        self.assertEqual(self.deck_object.deal_hand(53),self.cards)
        
    def test_deal_card(self):
        self.deck_object.deal_hand(53)
        #self.assertEqual(self.deck_object.count(),0)
        with self.assertRaises(ValueError):self.deck_object.deal_card()

if __name__ == '__main__':
    unittest.main()
