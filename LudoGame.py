# Author: Anthony Logan Clary
# GitHub username: alclary
# Date: August 4th, 2022
# Description: CS162 Portfolio Project

class Player:
    """represents the player who plays the game at a certain current_pos"""

    def __init__(self, player_letter):
        # hard-coded start and end points for respective players
        start_end = {
            'A':[1,50],
            'B':[15,8],
            'C':[29,49],
            'D':[43,36],
        }

        self._letter = player_letter # A, B, C, or D
        self._start = start_end[player_letter][0]
        self._end = start_end[player_letter][1]
        self._position = {
            'p':[-1,False], # token absolute location; T or F token in homerow
            'q':[-1,False]
        }
        self._state = None # PLAYING or FINISHED
        self._stacked = False # True if tokens stacked, else False

    def get_completed(self):
        """returns True or False if the player has finished or not finished the
            game

        Returns:
            bool: True if player has finished game, else false
        """
        return True if self._state == 'FINISHED' else False

    def set_token(self, token, current_pos):
        """setter method to set value of given token (p or q) [absolute
            location]

        Args:
            token (str): token to be set ('p' or 'q')
            current_pos (int): updated position to be set (-1 to 57 valid range)
        """
        if token == 'p':
            self._position['p'][0] = current_pos # token absolute location
        elif token == 'q':
            self._position['q'][0] = current_pos # token absolute location

    def get_token(self, token):
        """getter method to obtain given token's current position [absolute
            location]

        Args:
            token (str): token to retrieve value of ('p' or 'q')

        Returns:
            int: current position of given token
        """
        if token == 'p':
            return self.get_token_p_step_count() # token absolute location
        elif token == 'q':
            return self.get_token_q_step_count() # token absolute location

    def is_homerow(self, token):
        """return true if given token is currently located in the player's
            homerow

        Args:
            token (str): token to retrieve status of ('p' or 'q')

        Returns:
            bool: True if token is in homerow, else False
        """
        if token == 'p':
            return self._position['p'][1]
        elif token == 'q':
            return self._position['q'][1]

    def set_homerow(self, token, is_homerow):
        """set boolean value of given token, to indicate if currently in homerow

        Args:
            token (str): token to set status of ('p' or 'q')
            is_homerow (bool): True if token is in homerow, else False
        """
        if token == 'p':
            self._position['p'][1] = is_homerow
        elif token == 'q':
            self._position['q'][1] = is_homerow

    def is_stacked(self):
        """getter method to indicate if tokens for player are currently stacked

        Returns:
            bool: True if tokens are stacked, else False
        """
        return self._stacked

    def set_stacked(self, bool_val):
        """setter method to indicated/update if tokens for player are currently
            stacked

        Args:
            bool_val (bool): True if tokens are stacked, else False
        """
        self._stacked = bool_val

    def get_token_p_step_count(self):
        """returns the total steps the token p has taken on the board (uses
            steps = -1 for home yard current_pos and steps = 0 for ready to go
            current_pos)

        Returns:
            int: total steps the token p has taken
        """
        return self._position['p'][0]

    def get_token_q_step_count(self):
        """returns the total steps the token q has taken on the board (uses
            steps = -1 for home yard current_pos and steps = 0 for ready to go
            current_pos)

        Returns:
            int: total steps the token q has taken
        """
        return self._position['q'][0]

    def get_start(self):
        """getter method to return relative board starting place of player

        Returns:
            int: relative board starting place of player
        """
        return self._start

    def get_end(self):
        """getter method to return relative board end place of player

        Returns:
            int: relative board end place of player
        """
        return self._end

    def get_state(self):
        """getter method to return current state of player (e.g. None,
            'PLAYING', or 'FINISHED')

        Returns:
            None/string: current state of player
        """
        return self._state

    def set_state(self, new_state):
        """setter method to update current state of player (e.g. None,
            'PLAYING', or 'FINISHED')

        Args:
            new_state (None/string): updated state of player
        """
        self._state = new_state

    def get_space_name(self, total_steps):
        """takes as a parameter the total steps of the token and returns the
            name of the space the token has landed on on the board as a string.
            Returns 'H' for homeyard, 'R' for ready-to-go, 'F' for finish, and
            player-letter prefixed digits for homerow.

        Args:
            total_steps (int): total steps taken by a token for a given player

        Returns:
            string: letter or number (as string) designation of board space
        """
        pre_range = range(self._start, 57) # relative start through 56

        if total_steps == -1:
            return 'H'
        elif total_steps == 0:
            return 'R'
        elif total_steps == 57:
            return 'E'

        # If token in homerow
        elif total_steps in range(51, 57):
            return self._letter + str(total_steps - 50)

        # All other token locations (between relative start and finish)
        else:
            if self._letter == 'A':
                return str(total_steps)
            elif self._letter in ['B','C','D']:
                if total_steps + self._start - 1 in pre_range:
                    return str(total_steps + self._start - 1)
                else:
                    return str((total_steps - (56 - self._start)) - 1)

class LudoGame:
    """represents the game as played"""

    def __init__(self):
        self._active_players = {}

    def get_player_by_position(self, letter):
        """getter method to obtain Player object from given letter designation
            for player (e.g. 'A', 'B', 'C', or 'D')

        Args:
            letter (string): letter designation for player (e.g. A, B, C, or D)

        Returns:
            Player/string: player object or not found message
        """
        if letter in self._active_players.keys():
            return self._active_players[letter]
        else:
            return "Player not found!"

    def move_token(self, player, token, steps):
        """handles moving of given token on the board; also updates the token's
            total steps; and, calls additional methods to handle kicking and
            stacking, as needed.

        Args:
            player (Player): Player object
            token (string): token to be moved (e.g. 'p' or 'q')
            steps (int): number of steps to be moved
        """
        current_pos = player.get_token(token)

        # move token out of homeyard
        if current_pos == -1:
            if steps == 6:
                player.set_token(token, 0)

         # move token from ready space
        elif current_pos == 0:
            new_pos = steps

            self.handle_kick(player, new_pos)
            self.handle_stack(player, token, new_pos)
            player.set_token(token, new_pos)

        # move token within homerow
        elif current_pos in range(51, 57):
            new_pos = None
            if current_pos + steps == 57:
                new_pos = 57
            elif current_pos + steps < 57:
                new_pos = current_pos + steps
            elif current_pos + steps > 57:
                new_pos = (57 - (current_pos + steps)) + 57

            if player.is_stacked():
                player.set_token(token, new_pos)
                player.set_token(self.other_token(token), new_pos)
            else:
                player.set_token(token, new_pos)

        # move token that will go to homerow
        elif current_pos + steps in range(51, 57):
            new_pos = current_pos + steps
            if player.is_stacked():
                player.set_token(self.other_token(token), new_pos)
            else:
                self.handle_stack(player, token, new_pos)

            player.set_homerow(token, True)
            player.set_token(token, new_pos)

        # move all other tokens (1 to 45 (i.e. 51 - roll of 6))
        else:
            new_pos = current_pos + steps

            self.handle_kick(player, new_pos)
            if player.is_stacked() is True:
                player.set_token(token, new_pos)
                player.set_token(self.other_token(token), new_pos)
            else:
                self.handle_stack(player, token, new_pos)
                player.set_token(token, new_pos)

        self.check_finished()

    def handle_stack(self, initiator, token, new_pos):
        """method to assist in identifying and handling players stacking their
            tokens; if players other token is detected occupying the space that
            given token is moving to (new_pos), then Player object will be
            updated to indicate tokens are stacked.

        Args:
            initiator (Player): the player that is initiating the move
            token (string): token being moved (e.g. 'p' or 'q')
            new_pos (int): the new position the token will be moved to
        """
        if initiator.get_token(self.other_token(token)) == new_pos:
            initiator.set_stacked(True)
        return

    def handle_kick(self, initiator, new_pos):
        """method to assist in identifying and handling kicking of opponent back
            to homeyard; if opponent token is detected occupying the space that
            given token is moving to (new_pos), then opponent token will be
            'kicked' back to their homeyard.

        Args:
            initiator (Player): the player that is initiating the move
            new_pos (int): the new position the token will be moved tos
        """
        for player in self._active_players.values():
            if (player is not initiator and
                    player.get_space_name(player.get_token('p')) ==
                        initiator.get_space_name(new_pos) and
                    not player.is_homerow('p')):

                # Kick stacked moves BOTH token back to homeyard; only has to
                #   be tested once (in 'p' here) b/c tokens are linked
                if player.is_stacked():
                    player.set_token('p', -1)
                    player.set_token('q', -1)
                    return

                # Kick only opponent p token back
                else:
                    player.set_token('p', -1)
                    return

            # Kick on opponent q token back
            elif (player is not initiator and
                    player.get_space_name(player.get_token('q')) ==
                        initiator.get_space_name(new_pos) and
                    not player.is_homerow('q')):
                player.set_token('q', -1)
                return
        return

    def other_token(self, token):
        """helper function to quickly indicate opposite of given token
            i.e. if p, then q; if q, then p

        Args:
            token (string): given token (e.g. 'p' or 'q')

        Returns:
            string: opposite token (i.e. if p, then q; if q, then p)
        """
        if token == 'p':
            return 'q'
        elif token == 'q':
            return 'p'

    def check_finished(self):
        """function to identifying if win conditions have been met by a player
            and, if so, update Player object's state to 'FINISHED'
        """
        for player in self._active_players.values():
            if (player.get_token_p_step_count() == 57 and
                player.is_homerow('p') and
                player.get_token_q_step_count() == 57 and
                player.is_homerow('q')):
                player.set_state('FINISHED')

    def play_game(self, player_list, turns_list):
        """method creates the player list using the players list passed in; then
            moves tokens according to the given turns_list following the
            priority rule (set in token_to_move) and update the tokens
            current_pos and the player's game state.

        Args:
            player_list (list): list of player letters that will participate in
            game (e.g. ['A','B','C']) turns_list (list): list of tuples,
            specifying player letter and dice roll for turn (e.g. [('A':4),
            ('B':3),('A':6),('A':3)])

        Returns:
            list: a list of strings representing the current spaces of all of
            the tokens for each player
        """

        # Validate player list and create appropriate player objects;
        #   Player objects stored in self._active_players dict, by letter.
        self.player_create_validate(player_list)

        # iterate through given turns list
        for turn in turns_list:
            player_letter = turn[0]
            player = self._active_players[player_letter]
            roll = turn[1]

            if (player in self._active_players.values() and
                    player.get_state() == 'PLAYING'):
                token = self.token_to_move(player, roll)
                self.move_token(player, token, roll)

        current_board = []

        # iterate through current players so that positions can be returned
        for player in self._active_players.values():
            current_board.append(
                player.get_space_name(player.get_token_p_step_count()))
            current_board.append(
                player.get_space_name(player.get_token_q_step_count()))

        return current_board

    def player_create_validate(self, player_list):
        """function to validate and create active players for the for the
            LudoGame object, given the player_list passed from that function

        Args:
            player_list (list): list of player letters that will participate in
            game (e.g. ['A','B','C'])

        Raises:
            DuplicatePlayerError: indicates that same player is specified more
            than one or already exists
            PlayerLetterError: indicates that an item in player_list was not a
            one of the valid letters
        """
        try:
            for player in player_list:
                if player.upper() in ['A','B','C','D']:
                    if player.upper() in self._active_players:
                        raise DuplicatePlayerError
                    elif player.upper() not in self._active_players:
                        self._active_players[player.upper()] = Player(
                            player.upper())
                        self._active_players[player.upper()].set_state(
                            'PLAYING')
                else:
                    raise PlayerLetterError
        except PlayerLetterError:
            print("ERROR:  A player was specified without an appropriate" +
                    "letter.\n\tPlease ensure the player list only contains" +
                    "allowed letters (e.g. A, B, C, or D).")
        except DuplicatePlayerError:
            print("ERROR:  The same player was specified more than once. " +
                    "Please correct the player list.")

    def token_to_move(self, player, dice_roll):
        """decision algorithm, based on a priority ruleset, to decide which of
            given player's tokens should be moved next (e.g. 'p' or 'q').

        Args:
            player (Player): player whose token will be evaluated and moved
            dice_roll (int): dice roll, corresponding to number of steps token
                will move

        Returns:
            string: token that should be moved accoriding to priority ruleset
                (e.g. 'p' or 'q')
        """
        token_p = player.get_token_p_step_count()
        token_q = player.get_token_q_step_count()
        p_to_finish = 57 - token_p
        q_to_finish = 57 - token_q
        move_p_to_space = player.get_space_name(token_p + dice_roll)
        move_q_to_space = player.get_space_name(token_q + dice_roll)

        # TOKEN PRIORITY LOGIC

        # PRIORITY 1. If die roll is 6, try to let the token that still in
        #       home yard get out of yard (p first if both)
        if player.is_stacked() is True:
            return 'p'
        elif (dice_roll == 6 and
            (token_p == -1 or
            token_q == -1)):
            if token_p == -1: # token p has priority if both in home yard
                return 'p'
            elif token_q == -1:
                return 'q'

        # PRIORITY 2. If one token is already in the home square and the step
        #       number is exactly what is needed to reach the end square, let
        #       that token move and finish
        else:
            if dice_roll == p_to_finish:
                return 'p'
            elif dice_roll == q_to_finish:
                return 'q'

        # PRIORITY 3. If one token can move and kick out an opponent token,
        #       then move that token
            for active_player in self._active_players.values():
                if active_player is player:
                    continue
                else:
                    opponent_p = active_player.get_space_name(
                        active_player.get_token('p'))
                    opponent_q = active_player.get_space_name(
                        active_player.get_token('q'))
                    opp_p_homerow = active_player.is_homerow('p')
                    opp_q_homerow = active_player.is_homerow('q')
                    if move_p_to_space == opponent_p and not opp_p_homerow:
                        return 'p'
                    elif move_p_to_space == opponent_q and not opp_q_homerow:
                        return 'p'
                    elif move_q_to_space == opponent_p and not opp_p_homerow:
                        return 'q'
                    elif move_q_to_space == opponent_q and not opp_q_homerow:
                        return 'q'

        # PRIORITY 4. Move the token that is further away from the finishing
        #        square
            if p_to_finish > q_to_finish or token_q == -1:
                return 'p'
            else:
                return 'q'

class PlayerLetterError(Exception):
    """exception to indicate that an item in player_list was not a one of the
        valid letters"""
    pass

class DuplicatePlayerError(Exception):
    """excpetion to indicate that same player is specified more than one or
        already exists"""
    pass

def main():
    pass

if __name__ == '__main__':
    main()