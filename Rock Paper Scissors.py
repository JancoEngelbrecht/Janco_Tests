import random


def play():
    user = input("Rock, Paper, Scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Its\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return " You won!"

    return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


def rpsgame():
    human = input("Choose R P S: ")
    bot = random.choice(["r", "s", "p"])

    if human == bot:
        return "Tie!"

    # r > s, p > r, s > p
    if game(human, bot):
        return "You Win!"

    return 'You lost.'


def game(a, b):
    if (a == "r" and b == "s") or (a == "p" and b == "r") or (a == "s" and b == "p"):
        return True


print(rpsgame())
