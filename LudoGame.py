# Author: Anthony Logan Clary
# GitHub username: alclary
# Date: August 4th, 2022
# Description: CS162 Portfolio Project

class Player:
    """represents the player who plays the game at a certain position"""

    def __init__(self, player_letter):
        self._letter = player_letter # equivalent to player color
        self._start = None
        self._end = None
        self._position = None
        self._state = None

    def get_completed(self):
        # returns True or False if the player has finished or not finished the game
        pass

    def get_token_p_step_count(self):
        # takes no parameters and returns the total steps the token p has taken on the board (use
        # steps = -1 for home yard position and steps = 0 for ready to go position) The total step
        #  should not be larger than 57.
        pass

    def get_token_q_step_count(self):
        # takes no parameters and returns the total steps the token q has taken on the board (use
        # steps = -1 for home yard position and steps = 0 for ready to go position)
        pass

    def get_space_name(self, total_steps):
        # takes as a parameter the total steps of the token and returns the name of the space the
        # token has landed on on the board as a string. It should be able to return the home yard
        #  position (‘H’) and the ready to go position (‘R’) as well.
        pass

class LudoGame:
    """represents the game as played"""

    def __init__(self):
        pass

    def get_player_by_position(self, position):
        # takes a parameter representing the player's position as a string and returns
        #   the player object. For an invalid string parameter, it will return "Player not found!"
        pass

    def move_token(self, player, token, steps):
        # method will take care of one token moving on the board. It will also update the token’s
        # total steps, and it will take care of kicking out other opponent tokens as needed. The
        # play_game method will use this method.
        pass

    def play_game(self, player_list, turns_list):
        # The players list is the list of positions players choose, like [‘A’, ‘C’] means two players
        #  will play the game at position A and C. Turns list is a list of tuples with each tuple a
        #  roll for one player. For example, [('A', 6), ('A', 4), ('C', 5)] means player A rolls 6, then
        #  rolls 4, and player C rolls 5. This method will create the player list first using the players
        #  list pass in, and then move the tokens according to the turns list following the priority rule
        #  and update the tokens position and the player’s game state (whether finished the game or not).
        #  After all the moving is done in the turns list, the method will return a list of strings representing
        #  the current spaces of all of the tokens for each player in the list after moving the tokens following
        #  the rules described above. ‘H’ for home yard, ‘R’ for ready to go position, ‘E’ for finished
        #  position, and other letters/numbers for the space the token has landed on.
        pass

def main():
    pass

if __name__ == '__main__':
    main()