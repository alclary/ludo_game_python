# Author: Anthony Logan Clary
# GitHub username: alclary
# Date: August 4th, 2022
# Description: CS162 Portfolio Project

import unittest
from LudoGame import *

class TestKickInHomeRow(unittest.TestCase):
    def setUp(self):
        players = ['A', 'B']
        turns = [('A', 6), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), ('A', 5), # 5 x 11 = 55 = A5
                 ('B', 6), ('B', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 4), ('B', 1)] # 4 x 10 = 40 + 15 = 55
        game = LudoGame()
        game.play_game(players, turns)
        self.player_A = game.get_player_by_position('A')
        self.player_B = game.get_player_by_position('B')

    def test_A_not_kicked(self):
        self.assertEqual(self.player_A.get_token('p'), 55)

class TestGetSpaceName(unittest.TestCase):

if __name__ == '__main__':
  unittest.main()