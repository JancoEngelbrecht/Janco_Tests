import math
import random


class Player:  # Base Player Class/Parent Class. Build Players on top of this class by Inheritance
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move give a game

    def get_move(self, game):
        pass


# Derived Class/ Child Class
# Init is used to create a new object
# The child init overrides the inheritance of the parent's init.
# Super make the child inherit all the met4hods and properties of the parent
# No need to use the name of parent element when super is called. It automatically inherit the properties from the parent.
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # self.letter = letter

    def get_move(self, game):
        # Random choose in list from available indexes in file = Game, class function = available moves [1,5,4]
        square = random.choice(game.available_moves())
        return square  # Return Number [1]


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:  # While Valid_square is False
            square = input(self.letter + '\'s turn. Input (0-8):')
            # We're going to check that this is a correct value by trying to cast it to an integer,
            # and if it is not, then we say its invalid if that spot is not available on the board,
            # we also say its invalid.
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError  # If this is true is automatically skips to the except.
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)  # self.letter = letter, This allows you to call self.letter in this class.

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # Choose a random square at the beginning
        else:
            square = self.minimax(game, self.letter)['position']  # Otherwise run the minimax code
        return square

    def minimax(self, state, player):
        max_player = self.letter  # Yourself
        other_player = 'O' if player == 'X' else 'X'  # if player == x, then otherPlayer = O, if player =! x, then other_player = X

        if state.current_winner == other_player:  # This is actually game = state, therefore game.current_winner = X or O.
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                                state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares():  # If 0 (No empty_squares left)
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)
            # step 3: Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # step 4: Update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

            return best
