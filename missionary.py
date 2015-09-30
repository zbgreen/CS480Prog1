### File missionary.py
### Zachary Green
### CS 480 Prog1
### Implements the Missionary and Cannibals Problem for state space search

from search import *

class MissionaryState(ProblemState):
    """
    There are 3 missionaries and 3 cannibals on one side of a river. The
    objective is to get all of them to the other side using a boat that can
    carry 0-2 people at a time. The missionaries cannot be outnumbered at any
    time on either side or they will be eaten. Either missionaries or cannibals
    can operate the boat.

    lM = # of missionaries on left shore.
    lC = # of cannibals on left shore.
    bP = Boat position. '0' for left '1' for right.
    rM = # of missionaries on right shore.
    rC = # of cannibals on right shore.
    """
    def __init__(self, lM, lC, bP, rM, rC):
        self.lM = lM
        self.lC = lC
        self.bP = bP
        self.rM = rM
        self.rC = rC

    def __str__(self):
        """
        Required method for use with the Search class.
        :return:  Returns a string representation of the state.
        """
        return "(" + str(self.lM) + "," + str(self.lC) + "," + str(self.bP) + \
               "," + str(self.rM) + "," + str(self.rC) + ")"

    def illegal(self):
        """
        Required method for use with the Search class.
        :return: Returns 1 if illegal and 0 if legal.
        """
        #Check if less than 0 or more than 3 exist in the state.
        if self.lM < 0 or self.lM > 3: return 1
        if self.lC < 0 or self.lC > 3: return 1
        if self.rM < 0 or self.rM > 3: return 1
        if self.rC < 0 or self.rC > 3: return 1
        #Check if more cannibals are present than missionaries.
        #0 missionaries is a legal state.
        if (self.lM < self.lC) and self.lM > 0: return 1
        if (self.rM < self.rC) and self.rM > 0: return 1
        #Check if boat gets used incorrectly.
        if self.bP < 0 or self.bP > 1: return 1
        #legal state.
        return 0

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        :param compState: other state that is being compared to current state
        :return: Returns true is the same and false is not.
        """
        return self.lM == state.lM and self.lC == state.lC and self.bP == state.bP\
            and self.rM == state.rM and self.rC == state.rC

    def oneLMtoR(self):
        """
        Move 1 missionary to right.
        """
        return MissionaryState(self.lM - 1, self.lC, self.bP + 1, self.rM + 1, self.rC)

    def twoLMtoR(self):
        """
        Move 2 missionaries to right
        """
        return MissionaryState(self.lM - 2, self.lC, self.bP + 1, self.rM + 2, self.rC)

    def oneLCtoR(self):
        """
        Move 1 cannibal to right
        """
        return MissionaryState(self.lM, self.lC - 1, self.bP + 1, self.rM, self.rC + 1)

    def twoLCtoR(self):
        """
        Move 2 cannibals to right
        """
        return MissionaryState(self.lM, self.lC - 2, self.bP + 1, self.rM, self.rC + 2)

    def oneLMoneLCtoR(self):
        """
        Move 1 missionary and 1 cannibal to right
        """
        return MissionaryState(self.lM - 1, self.lC - 1, self.bP + 1, self.rM + 1, self.rC + 1)

    def oneRMtoL(self):
        """
        Move 1 missionary to the left
        """
        return MissionaryState(self.lM + 1, self.lC, self.bP - 1, self.rM - 1, self.rC)

    def twoRMtoL(self):
        """
        Move 2 missionaries to the left
        """
        return MissionaryState(self.lM + 2, self.lC, self.bP - 1, self.rM - 2, self.rC)

    def oneRCtoL(self):
        """
        Move 1 cannibal to the left
        """
        return MissionaryState(self.lM, self.lC + 1, self.bP - 1, self.rM, self.rC - 1)

    def twoRCtoL(self):
        """
        Move 2 cannibals to the left
        """
        return MissionaryState(self.lM, self.lC + 2, self.bP - 1, self.rM, self.rC - 2)

    def oneRMoneRCtoL(self):
        """
        Move 1 missionary and 1 cannibal to the left
        """
        return MissionaryState(self.lM + 1, self.lC + 1, self.bP - 1, self.rM - 1, self.rC - 1)

    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["oneLMtoR", "twoLMtoR", "oneLCtoR", "twoLCtoR", "oneLMoneLCtoR",
                "oneRMtoL", "twoRMtoL", "oneRCtoL", "twoRCtoL", "oneRMoneRMtoL"]

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.oneLMtoR(), self.twoLMtoR(), self.oneLCtoR(),
                self.twoLCtoR(), self.oneLMoneLCtoR(), self.oneRMtoL(),
                self.twoRMtoL(), self.oneRCtoL(), self.twoRCtoL(),
                self.oneRMoneRCtoL()]

#Test 3 missionaries and Cannibals on left side
Search(MissionaryState(3, 3, 0, 0, 0), MissionaryState(0, 0, 1, 3, 3))
