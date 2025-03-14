# this is simulation of the game obstgarten

import random

class Obstgarten:
    """
    Represents the game Obstgarten
    """

    def __init__(self):
        self.__obst = ["Apfel Rot", "Apfel Gruen", "Birne", "Pflaume"]
        self.__dice_badguy = "Rabe"
        self.__dice_choice = "Korb"
        self.__dice = list(self.__obst)
        self.__dice.extend([self.__dice_badguy, self.__dice_choice])
        self.reset()

    def reset(self):
        self._trees = dict([(obst, 4) for obst in self.__obst])
        self._raven = 6


    def play(self):
        """
        Simulates a full round of play, including taking the optimal choices
        @return: True if Players win, False if Players loose
        """
        
        self.reset()

        while True:

            # Check loose/win conditions
            if self._raven <= 0:
                return False

            if sum(self._trees.values()) <= 0:
                return True

            self._play_single_round()
    
    def _play_single_round(self):

        dice = random.choice(self.__dice)

        if dice in self._trees:
            self._trees[dice] -= 1
            return 

        if dice == self.__dice_badguy:
            self._raven -= 1
            return 
        
        if dice == self.__dice_choice:
            # we freely can choose from the existing trees. Strategy: take the one with the most entries
            max_tree_item = max(self._trees.items(), key=lambda tree_item: tree_item[1])
            self._trees[max_tree_item[0]] -= 1
            return 
            


def simulate(rounds_count = 10000):
    game = Obstgarten()

    win_count = 0

    for _ in range(rounds_count):
        if game.play():
            win_count += 1

    return win_count

def main():
    result = simulate(10000)

    print(f"Won {result} times out of 10000")

if __name__ == "__main__": main()
#EOF