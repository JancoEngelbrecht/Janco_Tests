import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_winner = None  # Keep track of the winner

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            # indexing board list [0:3], [3:6], [6:9]
            # ' ', ' ', ' '
            # ' ', ' ', ' '
            # ' ', ' ', ' '

            print('| ' + ' | '.join(row) + ' |')  # Use ' | ' as the separator

            # join.row  = Joins the list into a string and uses the separator between the items
            #  ' ' | ' ' | ' '
            #  ' ' | ' ' | ' '
            #  ' ' | ' ' | ' '

            # print
            # | ' ' | ' ' | ' ' |
            # | ' ' | ' ' | ' ' |
            # | ' ' | ' ' | ' ' |

    @staticmethod  # When we do not want subclasses of a class to change or override a specific implementation method
    def print_board_nums():
        # 0 | 1 | 2 ect tells us what number corresponds to what box
        # This function is only printed at the start of the game
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]

        # indexing board list [0:3], [3:6], [6:9]
        # return each number as a string in a list
        # 0, 1, 2
        # 3, 4, 5
        # 6, 7, 8

        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

            # | 0 | 1 | 2 |
            # | 3 | 4 | 5 |
            # | 6 | 7 | 8 |

    def available_moves(self):
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):  # enumerate = ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]

            # example of one loop (i, spot) = (0,' ')

            if spot == ' ':
                moves.append(i)

                # Spot = ' ' --> moves = [0,]

        return moves  # Returns [0] as available moves

    def empty_squares(self):
        return ' ' in self.board  # List of ' '

    def num_empty_squares(self):
        return self.board.count(' ')  # Counts the empty_squares in the list --> 3

    #                   ( 5   ,   O  )
    def make_move(self, square, letter):
        # if valid move then make the move (assign square to letter)
        # then return true. if invalid, return false
        #             [ 5 ]
        if self.board[square] == ' ':  # if the selected square is ' ',
            #           [ 5 ]  =   'O'
            self.board[square] = letter  # then replace the square with the letter
            # | ' ' | ' ' | ' ' |
            # | ' ' | '5' | ' ' |
            # | ' ' | ' ' | ' ' |

            # Pass the move into winner function
            #                ( 5   ,   O )
            if self.winner(square, letter):
                #                   =  '0'
                self.current_winner = letter
            return True
        return False

    #                ( 5   ,   O )
    def winner(self, square, letter):  # Pass in Square Number and Square Letter

        # Check row
        #           [5] // 3 = 1
        row_ind = square // 3  # Square Index number divided by 3 and then floored.
        #                  [1]           [1]
        row = self.board[row_ind * 3: (row_ind + 1) * 3]

        # 1*3 = 3  : (1+1) * 3 = 6
        # self.board [3:6] = [3, 4, 5]

        #         3  ==  "O"   for 3 in [3, 4, 5]
        if all([spot == letter for spot in row]):  # If [1=X,2=X,3=X] is means All == True, therefore Return True.
            #  All checks that all the items in a list is the same value, and then returns true or false.
            return True

        # Check Column
        col_ind = square % 3  # Modulo = %

        # 1/3 = (3 can't go into 1 therefore = 0) (The Remainder of 1 remains)
        # Quotient * Divisor * Remainder = Dividend
        # 0 * 3 + 1 = 1

        # 2/3 = 0 (Remainder of 2)
        # 0 * 3 + 2 = 2

        # 3/3 = 1 (Remainder of 0)
        # 1 * 3 + 0 = 3

        column = [self.board[col_ind + i * 3] for i in range(3)]
        # Range 3 = 0, 1, 2
        # 1+0*3 = 1
        # 1+1*3 = 4
        # 1+2*3 = 7

        if all([spot == letter for spot in column]):
            return True

        # Check Diagonal
        if square % 2 == 0:
            # [0, 2, 4, 6, 8] % 2 = 0
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            # self.board[0]
            # self.board[4]
            # self.board[8]

            if all([spot == letter for spot in diagonal1]):
                # self.board[0] = 'X'
                # self.board[4] = 'X'
                # self.board[8] = 'X'

                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            # self.board[2]
            # self.board[4]
            # self.board[6]

            if all([spot == letter for spot in diagonal2]):
                # self.board[2] = 'X'
                # self.board[4] = 'X'
                # self.board[6] = 'X'

                return True

        # if all of the checks fail
        return False


def play(game, x_player, o_player, print_game=True):  # Pass in Class TicTacToe as Game, then you can call TicTacToe functions by using game.function
    # returns the winner of the game( or the letter)! or None for a tie

    if print_game:  # If True is passed into print_game
        game.print_board_nums()  # print the board with the numbers
        # | 0 | 1 | 2 |
        # | 3 | 4 | 5 |
        # | 6 | 7 | 8 |

    letter = 'X'  # starting letter

    while game.empty_squares():
        # [' ', ' ', ' ']

        if letter == 'O':
            square = o_player.get_move(game)
            # square = [5] for example


        else:
            square = x_player.get_move(game)
            # square = [2] for example

        #                 ( 5   ,   O  )
        if game.make_move(square, letter):

            if print_game:  # if print game true
                #       'O'  makes a move to square 5
                print(letter + f' makes a move to square {square}')
                #
                game.print_board()
                print('')  # just empty line

                # | ' ' | ' ' | ' ' |
                # | ' ' | '5' | ' ' |
                # | ' ' | ' ' | ' ' |
                # empty line

            if game.current_winner:  # If game.current_winner in def available_moves returns True, then if print game is true, then print who won.
                # Otherwise just skip this section
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move, we need to alternate letters
            # letter = 'O' if letter == 'X' else 'X'
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'

            # tiny Break for readability
            if print_game:
                time.sleep(0.8)

    # If the game breaks out of the loop, because all the empty squares have been filled, then print tie.3

    if print_game:
        print('It is a Tie')


if __name__ == '__main__':  # Ensures that the functions below only run when this file is run directly.
    # When you import classes like above, their __name__ = their file name if they are not run directly, but as part of this file.
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(100):
        x_player = RandomComputerPlayer('X')  # This is assigning the class HumanPlayer to x_player and passing in X = Letter
        o_player = GeniusComputerPlayer('O')  # This is assigning the class RandomComputerPlayer to o_player and passing in O = Letter
        t = TicTacToe()  # This is just assigning the TicTacToe Class to "t"
        result = play(t, x_player, o_player,
                      print_game=False)  # This is calling game and here we import all the parts into the main function
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties')
