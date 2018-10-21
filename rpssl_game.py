"""
After
@ Clever Programmer
Rock paper scissors
"""
import random

# Global variables that all functions know about.
# DO NOT EDIT THESE GLOBAL VARIABLES
# OR YOUR GAME WILL BREAK.
COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""


def choice_to_number(choice):
    """Convert choice to number."""

    # TODO: Implement

    raise NotImplementedError


def number_to_choice(number):
    """Convert number to choice."""

    # TODO: Implement

    raise NotImplementedError


def random_computer_choice():
    """Choose randomly for computer."""

    # TODO: Implement (Hint: Look up random.choice())

    raise NotImplementedError


def choice_result(human_choice, computer_choice):
    """Return the result of who wins."""

    # DO NOT REMOVE THESE GLOBAL VARIABLE LINES.
    global COMPUTER_SCORE
    global HUMAN_SCORE

    # TODO: Implement
    # Based on the given human_choice and computer_choice,
    # determine who won and increment their score by 1.
    # In case of tie, don't increment anyone's score.

    # NOTE
    # A modulo-based solution (see Clever Programmer tutorial and assignment README) will be preferred.
    # Evaluation will be as follows:
    # 1. Modulo-based solution: 100%
    # 2. Chain-of-if-statements solution: 80%

    raise NotImplementedError


# DO NOT REMOVE THESE TEST FUNCTIONS.
# They will test your code.
def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2


def test_number_to_choice():
    assert number_to_choice(0) == 'rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'


def test_computer_choice():
    choice = random_computer_choice()
    assert choice in ['rock', 'paper', 'scissors', 'spock', 'lizard']
    assert 0 <= choice_to_number(choice) <= 4


def test_all():
    test_choice_to_number()
    test_number_to_choice()
    test_computer_choice()


# Uncomment to test your functions.
# test_all()


# Code for handling human player moves
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)


def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)


def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)


def spock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'spock'
    choice_result(human_choice, computer_choice)


def lizard():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'lizard'
    choice_result(human_choice, computer_choice)


# Game play functions
def greet():
    print('Welcome to the game of RPSSL')
    print('Commands: (r)ock\n' +
          '          (p)aper\n' +
          '          (s)cissors\n' +
          '          sp(o)ck\n' +
          '          (l)izard\n' +
          '          (q)uit\n')


def get_user_input():
    valid = False
    while not valid:
        print('Please, make a choice: ', end='')
        s = input().strip().lower()
        if len(s) > 1 or s not in 'rpsolq':
            print('Invalid input. Valid inputs are {r, p, s, o, l, q}.')
            continue
        else:
            return s


def play_rps():
    global HUMAN_SCORE, COMPUTER_SCORE

    moves = {'r': rock,
             'p': paper,
             's': scissors,
             'o': spock,
             'l': lizard}
    greet()
    while True:
        user_input = get_user_input()
        if user_input == 'q':
            print('Final score: Human {} : Computer {}'.format(HUMAN_SCORE, COMPUTER_SCORE))
            print('Thanks for playing. Good bye!')
            break
        else:
            move = moves.get(user_input)
            assert move is not None
            move()
            print('Score: Human {} : Computer {}'.format(HUMAN_SCORE, COMPUTER_SCORE))


if __name__ == '__main__':
    play_rps()
