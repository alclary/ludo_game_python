# Author: Anthony Logan Clary
# GitHub username: alclary
# Date: August 4th, 2022
# Description: CS162 Portfolio Project

class Player:
    """represents the player who plays the game at a certain current_pos"""

    def __init__(self, player_letter):
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
            'p':[-1,False],
            'q':[-1,False]
        }
        self._state = None # PLAYING or FINISHED
        self._stacked = False # T or F if tokens stacked

    def get_completed(self):
        # returns True or False if the player has finished or not finished the game
        return True if self._state == 'FINISHED' else False

    def set_token(self, token, current_pos):
        if token == 'p':
            self._position['p'][0] = current_pos
        elif token == 'q':
            self._position['q'][0] = current_pos

    def get_token(self, token):
        if token == 'p':
            return self.get_token_p_step_count()
        elif token == 'q':
            return self.get_token_q_step_count()

    def is_homerow(self, token):
        if token == 'p':
            return self._position['p'][1]
        elif token == 'q':
            return self._position['q'][1]

    def set_homerow(self, token, is_homerow):
        if token == 'p':
            self._position['p'][1] = is_homerow
        elif token == 'q':
            self._position['q'][1] = is_homerow

    def is_stacked(self):
        return self._stacked

    def set_stacked(self, bool_val):
        self._stacked = bool_val

    def get_token_p_step_count(self):
        # takes no parameters and returns the total steps the token p has taken on the board (use
        # steps = -1 for home yard current_pos and steps = 0 for ready to go current_pos) The total step
        # should not be larger than 57.
        return self._position['p'][0]

    def get_token_q_step_count(self):
        # takes no parameters and returns the total steps the token q has taken on the board (use
        # steps = -1 for home yard current_pos and steps = 0 for ready to go current_pos)
        return self._position['q'][0]

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_state(self):
        return self._state

    def set_state(self, state_update):
        self._state = state_update

    def get_space_name(self, total_steps):
        # takes as a parameter the total steps of the token and returns the name of the space the
        # token has landed on on the board as a string. It should be able to return the home yard
        # current_pos (‘H’) and the ready to go current_pos (‘R’) as well.
        relative_range = range(self._start, self._start + 50)
        homerow = range(self._end + 1, self._end + 6)
        finish = self._end + 7

        if total_steps == -1:
            return 'H'
        elif total_steps == 0:
            return 'R'
        elif total_steps in relative_range and total_steps < 56 - self._start:
            return str((total_steps + self._start) - 1)
        elif total_steps in relative_range and total_steps > 56 - self._start:
            return str((total_steps - (56 - self._start)) - 1)
        elif total_steps in homerow:
            return self._letter + str(total_steps - 50)
        elif total_steps == finish:
            return 'F'

class LudoGame:
    """represents the game as played"""

    def __init__(self):
        self._active_players = {}
        self._pos_key = {
            'H': -1,
            'R': 0,
            'F': 57,
            }

    def get_player_by_position(self, letter):
        if letter in self._active_players.keys():
            return self._active_players[letter]   # Shortcut to player obj via letter (A,B,C,D)
        else:
            return "Player not found!"

    def move_token(self, player, token, steps):
        # method will take care of one token moving on the board. It will also update the token’s
        # total steps, and it will take care of kicking out other opponent tokens as needed. The
        # play_game method will use this method.

        current_pos = player.get_token(token)
        start = player.get_start()
        end = player.get_end()
        finish = end + 7

        # 1. Move token (update player)
        if current_pos == -1:
            if steps == 6:
                player.set_token(token, 0)

        elif current_pos == 0:
            new_pos = (start + steps) - 1
            self.handle_kick(player, new_pos)
            self.handle_stack(player, token, new_pos)
            player.set_token(token, new_pos)

        elif current_pos in range(end + 1, end + 6):
            new_pos = None
            if current_pos + steps == finish:
                new_pos = finish
            elif current_pos + steps < finish:
                new_pos = current_pos + steps
            elif current_pos + steps > finish:
                new_pos = (finish - (current_pos + steps)) + finish

            if player.is_stacked():
                player.set_token(token, new_pos)
                player.set_token(self.other_token(token), new_pos)
            else:
                player.set_token(token, new_pos)

        elif current_pos + steps in range(end + 1, end + 6):
            new_pos = current_pos + steps
            if player.is_stacked():
                player.set_token(self.other_token(token), new_pos)
            else:
                self.handle_stack(player, token, new_pos)

            player.set_homerow(token, True)
            player.set_token(token, new_pos)

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
        if initiator.get_token(self.other_token(token)) == new_pos:
            initiator.set_stacked(True)
        return

    def handle_kick(self, initiator, new_pos):
        for player in self._active_players.values():
            if (player is not initiator and
                    player.get_token('p') == new_pos and
                    not player.is_homerow('p')):
                if player.is_stacked():
                    player.set_token('p', -1)
                    player.set_token('q', -1)
                else:
                    player.set_token('p', -1)
            elif (player is not initiator and
                    player.get_token('q') == new_pos and
                    not player.is_homerow('q')):
                player.set_token('q', -1)
        return

    def other_token(self, token):
        if token == 'p':
            return 'q'
        elif token == 'q':
            return 'p'

    def check_finished(self):
        for player in self._active_players.values():
            end = player.get_end()
            finish = end + 7
            if (player.get_token_p_step_count() == finish and
                player.is_homerow('p') and
                player.get_token_q_step_count() == finish and
                player.is_homerow('q')):
                player.set_state('FINISHED')

    def play_game(self, player_list, turns_list):
        # The players list is the list of positions players choose, like [‘A’, ‘C’] means two players
        #  will play the game at current_pos A and C. Turns list is a list of tuples with each tuple a
        #  roll for one player. For example, [('A', 6), ('A', 4), ('C', 5)] means player A rolls 6, then
        #  rolls 4, and player C rolls 5. This method will create the player list first using the players
        #  list pass in, and then move the tokens according to the turns list following the priority rule
        #  and update the tokens current_pos and the player’s game state (whether finished the game or not).
        #  After all the moving is done in the turns list, the method will return a list of strings representing
        #  the current spaces of all of the tokens for each player in the list after moving the tokens following
        #  the rules described above. ‘H’ for home yard, ‘R’ for ready to go current_pos, ‘E’ for finished
        #  current_pos, and other letters/numbers for the space the token has landed on.

        self.player_create_validate(player_list)

        for turn in turns_list:
            player_letter = turn[0]
            player = self._active_players[player_letter]
            roll = turn[1]

            if (player in self._active_players.values() and
                player.get_state() == 'PLAYING'):
                token = self.token_to_move(player, roll)
                self.move_token(player, token, roll)
                print(player_letter + " - " + token + ': ' + str(player.get_token(token)) + ", "
                    + self.other_token(token) + ": " + str(player.get_token(self.other_token(token))))  # TODO Remove DEBUG print log

        current_board = []

        for player in self._active_players.values():
            current_board.append(player.get_space_name(player.get_token_p_step_count()))
            current_board.append(player.get_space_name(player.get_token_q_step_count()))

        return current_board

    def player_create_validate(self, player_list):
        try:
            for player in player_list:
                if player.upper() in ['A','B','C','D']:
                    if player.upper() in self._active_players:
                        raise DuplicatePlayerError
                    elif player.upper() not in self._active_players:
                        self._active_players[player.upper()] = Player(player.upper())
                        self._active_players[player.upper()].set_state('PLAYING')
                else:
                    raise PlayerLetterError
        except PlayerLetterError:
            print("ERROR:  A player was specified without an appropriate letter.\n\t" +
                    "Please ensure the player list only contains allowed letters (e.g. A, B, C, or D).")
        except DuplicatePlayerError:
            print("ERROR:  The same player was specified more than once. Please correct the player list.")

    def token_to_move(self, player, dice_roll):
        #  decision-making algorithm for a player to choose a certain token to move.
        token_p = player.get_token_p_step_count()
        token_q = player.get_token_q_step_count()
        p_to_finish = 57 - token_p
        q_to_finish = 57 - token_q
        move_p_to = token_p + dice_roll
        move_q_to = token_q + dice_roll

        # TOKEN PRIORITY LOGIC
        # 1. If die roll is 6, try to let the token that still in home yard get out of yard (p first if both)
        if player.is_stacked() is True:
            return 'p'
        elif (dice_roll == 6 and
            (token_p == -1 or
            token_q == -1)):
            if token_p == -1: # token p has priority if both in home yard
                return 'p'
            elif token_q == -1:
                return 'q'
        else:
            # 2. If one token is already in the home square and the step number is exactly what is
            #   needed to reach the end square, let that token move and finish
            if dice_roll == p_to_finish:
                return 'p'
            elif dice_roll == q_to_finish:
                return 'q'


            # if (self.get_player_by_position(player.get_space_name(token_p + dice_roll)) is not None and
            #         token_p != -1):
            #     return 'p'
            # elif (self.get_player_by_position(player.get_space_name(token_q + dice_roll)) is not None and
            #         token_q != -1):
            #     return 'q'
            # 3. If one token can move and kick out an opponent token, then move that token

            for active_player in self._active_players.values():
                if active_player is player:
                    continue
                else:
                    opponent_p = active_player.get_token('p')
                    opponent_q = active_player.get_token('q')
                    opp_p_homerow = active_player.is_homerow('p')
                    opp_q_homerow = active_player.is_homerow('q')
                    if move_p_to == opponent_p and not opp_p_homerow:
                        return 'p'
                    elif move_p_to == opponent_q and not opp_q_homerow:
                        return 'p'
                    elif move_q_to == opponent_p and not opp_p_homerow:
                        return 'q'
                    elif move_q_to == opponent_q and not opp_q_homerow:
                        return 'q'

            # 4. Move the token that is further away from the finishing square
            if p_to_finish > q_to_finish or token_q == -1:
                return 'p'
            else:
                return 'q'

class PlayerLetterError(Exception):
    pass

class DuplicatePlayerError(Exception):
    pass

def main():
    players = ['A', 'B']
    turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
    game = LudoGame()
    current_tokens_space = game.play_game(players, turns)
    # player_A = game.get_player_by_position('A')
    # print(player_A.get_completed())
    # print(player_A.get_token_p_step_count())
    # print(current_tokens_space)
    player_B = game.get_player_by_position('B')
    print(player_B.get_space_name(55))

if __name__ == '__main__':
    main()