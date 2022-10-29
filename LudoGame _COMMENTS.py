# Author: Anthony Logan Clary
# GitHub username: alclary
# Date: August 4th, 2022
# Description: CS162 Portfolio Project

class Player:
    """represents the player who plays the game at a certain current_pos"""

    def __init__(self, player_letter):
        """The constructor for Player class. Takes no parameters. Initializes the required
            data members. All data members are private.
        """
        pass

    def get_completed(self):
        """returns True or False if the player has finished or not finished the game

        Returns:
            bool: True if player has finished game, else false
        """
        pass

    def set_token(self, token, current_pos):
        """setter method to set value of given token (p or q)

        Args:
            token (str): token to be set ('p' or 'q')
            current_pos (int): updated position to be set (-1 to 57 valid range)  # TODO confirm correct
        """
        pass

    def get_token(self, token):
        """getter method to obtain given token's current position

        Args:
            token (str): token to retrieve value of ('p' or 'q')

        Returns:
            int: current position of given token
        """
        pass

    def is_homerow(self, token):
        """return true if given token is currently located in the player's homerow

        Args:
            token (str): token to retrieve status of ('p' or 'q')

        Returns:
            bool: True if token is in homerow, else False
        """
        pass

    def set_homerow(self, token, is_homerow):
        """set boolean value of given token, to indicate if currently in homerow

        Args:
            token (str): token to set status of ('p' or 'q')
            is_homerow (bool): True if token is in homerow, else False
        """
        pass

    def is_stacked(self):
        """getter method to indicate if tokens for player are currently stacked

        Returns:
            bool: True if tokens are stacked, else False
        """
        pass

    def set_stacked(self, bool_val):
        """setter method to indicated/update if tokens for player are currently stacked

        Args:
            bool_val (bool): True if tokens are stacked, else False
        """
        pass

    def get_token_p_step_count(self):
        """returns the total steps the token p has taken on the board (uses steps = -1 for
            home yard current_pos and steps = 0 for ready to go current_pos)

        Returns:
            int: total steps the token p has taken
        """
        pass

    def get_token_q_step_count(self):
        """returns the total steps the token q has taken on the board (uses steps = -1 for
            home yard current_pos and steps = 0 for ready to go current_pos)

        Returns:
            int: total steps the token q has taken
        """
        pass

    def get_start(self):
        """getter method to return relative board starting place of player

        Returns:
            int: relative board starting place of player
        """
        pass

    def get_end(self):
        """getter method to return relative board end place of player

        Returns:
            int: relative board end place of player
        """
        pass

    def get_state(self):
        """getter method to return current state of player (e.g. None, 'PLAYING', or 'FINISHED')

        Returns:
            None/string: current state of player
        """
        pass

    def set_state(self, new_state):
        """setter method to update current state of player (e.g. None, 'PLAYING', or 'FINISHED')

        Args:
            new_state (None/string): updated state of player
        """
        pass

    def get_space_name(self, total_steps):
        """takes as a parameter the total steps of the token and returns the name of the space the
            token has landed on on the board as a string. Returns 'H' for homeyard, 'R' for ready-to-go,
            'F' for finish, and player-letter prefixed digits for homerow.

        Args:
            total_steps (int): total steps taken by a token for a given player

        Returns:
            string: letter or number (as string) designation of board space
        """
        pass

class LudoGame:
    """represents the game as played"""

    def __init__(self):
        """The constructor for LudoGame class. Takes no parameters. Initializes the required
            data members. All data members are private.
        """
        pass

    def get_player_by_position(self, letter):
        """getter method to obtain Player object from given letter designation for player (e.g. 'A', 'B', 'C', or 'D')

        Args:
            letter (string): letter designation for player (e.g. A, B, C, or D)

        Returns:
            Player/string: player object or not found message
        """
        pass

    def move_token(self, player, token, steps):
        """handles moving of given token on the board; also updates the token's total steps;
            and, calls additional methods to handle kicking and stacking, as needed.

        Args:
            player (Player): Player object
            token (string): token to be moved (e.g. 'p' or 'q')
            steps (int): number of steps to be moved
        """
        pass

    def handle_stack(self, initiator, token, new_pos):
        """method to assist in identifying and handling players stacking their tokens;
            if players other token is detected occupying the space that given token is
            moving to (new_pos), then Player object will be updated to indicate tokens
            are stacked.

        Args:
            initiator (Player): the player that is initiating the move
            token (string): token being moved (e.g. 'p' or 'q')
            new_pos (int): the new position the token will be moved to
        """
        pass

    def handle_kick(self, initiator, new_pos):
        """method to assist in identifying and handling kicking of opponent back to homeyard;
            if opponent token is detected occupying the space that given token is moving to
            (new_pos), then opponent token will be 'kicked' back to their homeyard.

        Args:
            initiator (Player): the player that is initiating the move
            new_pos (int): the new position the token will be moved tos
        """
        pass

    def other_token(self, token):
        """helper function to quickly indicate opposite of given token
            i.e. if p, then q; if q, then p

        Args:
            token (string): given token (e.g. 'p' or 'q')

        Returns:
            string: opposite token (i.e. if p, then q; if q, then p)
        """
        pass

    def check_finished(self):
        """function to identifying if win conditions have been met by a player and, if so,
            update Player object's state to 'FINISHED'
        """
        pass

    def play_game(self, player_list, turns_list):
        """method creates the player list using the players list passed in; then moves tokens according
            to the given turns_list following the priority rule (set in token_to_move) and update the
            tokens current_pos and the player's game state.

        Args:
            player_list (list): list of player letters that will participate in game (e.g. ['A','B','C'])
            turns_list (list): list of tuples, specifying player letter and dice roll for turn
                (e.g. [('A':4),('B':3),('A':6),('A':3)])

        Returns:
            list: a list of strings representing the current spaces of all of the tokens for each player
        """
        pass

    def player_create_validate(self, player_list):
        """function to validate and create active players for the for the LudoGame object,
            given the player_list passed from that function

        Args:
            player_list (list): list of player letters that will participate in game (e.g. ['A','B','C'])

        Raises:
            DuplicatePlayerError: indicates that same player is specified more than one or already exists
            PlayerLetterError: indicates that an item in player_list was not a one of the valid letters
        """
        pass

    def token_to_move(self, player, dice_roll):
        """decision algorithm, based on a priority ruleset, to decide which of given player's
            token should be moved next (e.g. 'p' or 'q').

        Args:
            player (Player): player whose token will be evaluated and moved
            dice_roll (int): dice roll, corresponding to number of steps token will move

        Returns:
            string: token that should be moved accoriding to priority ruleset (e.g. 'p' or 'q')
        """
        pass

class PlayerLetterError(Exception):
    """exception to indicate that an item in player_list was not a one of the valid letters"""
    pass

class DuplicatePlayerError(Exception):
    """excpetion to indicate that same player is specified more than one or already exists"""
    pass

def main():
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    player_A = game.get_player_by_position('A')
    print(player_A.get_completed())
    print(player_A.get_token_p_step_count())
    print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(55))

if __name__ == '__main__':
    main()