### File eightPuzzle.py
### Implements the eight puzzle problem for state space search

from informedSearch import *

class PuzzleState(ProblemState):
    """
    The state of the puzzle is a 3x3 matrix of numbers 1-8. The printed goal
    state will look like this:
    1 2 3
    8   4
    7 6 5
    The objective is when given a non-goal state to swap a number with the
    black space to reach the goal state. No diagonal moves are allowed and
    moves cannot be made to wrap around the board.

    Data Structure(goal state):
    [1, 2, 3, 8, 0, 4, 7, 6, 5]
    """