### File eightPuzzle.py
### Zachary Green
### CS 480 Prog1
### Implements the eight puzzle problem for state space search

from informedSearch import *

class PuzzleState(InformedProblemState):
    """
    The state of the puzzle is a 3x3 matrix of numbers 1-8. The goal state will
    look like this:
    1 2 3
    8 0 4
    7 6 5
    The objective is when given a non-goal state to swap a number with the
    black space to reach the goal state. No diagonal moves are allowed and
    moves cannot be made to wrap around the board.

    Data Structures:
    puz (eight puzzle) = '123804765'
    0: the empty space

                Node Expansions
    Problem     BFS     A*(tiles)   A*(dist)
    a           4       3           3
    b           77      8           7
    c           179     18          10
    d           666     48          20
    e           809     44          20
    f           1843    110         123
    g           5396    375         61
    h           48707   3290        186
    """
    def __init__(self, puz):
        self.puz = puz

    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return self.puz

    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal. Illegal states return -1 from the
        operator.
        """
        if self.puz == -1:
            return 1
        return 0

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.puz == state.puz

    def movL(self):
        """
        Moves zero value one space left. If it is in the left column it will
        return -1
        """
        i = self.puz.index('0')
        if i not in (0, 3, 6):
            index = i - 1
            newPuz = ""
            newPuz = self.puz[0:index] + '0' + self.puz[index] + self.puz[i + 1:]
            return PuzzleState(newPuz)
        return PuzzleState(-1)

    def movR(self):
        """
        Moves zero value one space right. If it is in the right column it will
        return -1
        """
        i = self.puz.index('0')
        if i not in (2, 5, 8):
            j = i + 1
            newPuz = ""
            newPuz = self.puz[0:i] + self.puz[j] + '0' + self.puz[j + 1:]
            return PuzzleState(newPuz)
        return PuzzleState(-1)

    def movUp(self):
        """
        Moves zero value one space up. If it is in the top row it will return
        -1
        """
        i = self.puz.index('0')
        if i not in (0, 1, 2):
            j = i - 3
            newPuz = ""
            newPuz = self.puz[0:j] + '0' + self.puz[j + 1: i] + self.puz[j] + self.puz[i + 1:]
            return PuzzleState(newPuz)
        return PuzzleState(-1)

    def movDn(self):
        """
        Moves zero value one space up. If it is in the bottom row it will
        return -1
        """
        i = self.puz.index('0')
        if i not in (6, 7, 8):
            j = i + 3
            newPuz = ""
            newPuz = self.puz[0: i] + self.puz[j] + self.puz[i + 1: j] + '0' + self.puz[j + 1:]
            return PuzzleState(newPuz)
        return PuzzleState(-1)

    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["movL", "movR", "movUp", "movDn"]

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.movL(), self.movR(), self.movUp(), self.movDn()]

    def heuristic(self, goal):
        """
        Required method for use with InformedSearch class.
        Executes Manhattan Distance, Tiles Out of Place  or Breadth First
        Search heuristics.
        """
        #sum = 0
        #sum = PuzzleState.outOfPlace(self, goal
        sum = PuzzleState.manhattan(self, goal)
        return sum

    def manhattan(self, goal):
        """
        Finds the Manhattan Distance (up, down, left, right distance) from
        the goal state for each value of the matrix and returns the sum.
        """
        sum = 0
        for i in goal.puz:
            sum += abs(self.puz.index(i) - goal.puz.index(i))
        return sum

    def outOfPlace(self, goal):
        """
        Returns the number of values out of place from the matrix.
        """
        sum = 0
        for i in range(0, 9):
            if self.puz[i] != goal.puz[i]:
                sum += 1
        return sum

goal = '123804765'
a = '130824765'
b = '134862075'
c = '013425876'
d = '712803654'
e = '812704653'
f = '263405187'
g = '734615802'
h = '745603812'

InformedSearch(PuzzleState(a), PuzzleState(goal))
InformedSearch(PuzzleState(b), PuzzleState(goal))
InformedSearch(PuzzleState(c), PuzzleState(goal))
InformedSearch(PuzzleState(d), PuzzleState(goal))
InformedSearch(PuzzleState(e), PuzzleState(goal))
InformedSearch(PuzzleState(f), PuzzleState(goal))
InformedSearch(PuzzleState(g), PuzzleState(goal))
InformedSearch(PuzzleState(h), PuzzleState(goal))
