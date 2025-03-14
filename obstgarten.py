# this is simulation of the game obstgarten

import random

class Obstgarten:
    """
    Represents the game Obstgarten
    """

    def __init__(self, obst_count = 4, raven_count = 6, choice_selection = 1):
        """
        @obst_count:       Wie viele Apfel/Birnen/... hat jeder Baum?
        @raven_count:      Wie viele Schritte muss der Rabe gehen, bevor er die Baeume erreicht?
        @choice_selection: Wenn man den Korb wuerfelt, wieviel Obst darf man nehmen?
        """
        self.__obst = ["Apfel Rot", "Apfel Gruen", "Birne", "Pflaume"]
        self.__dice_badguy = "Rabe"
        self.__dice_choice = "Korb"
        self.__dice = self.__obst + [self.__dice_badguy, self.__dice_choice]
        self.__obst_count = obst_count
        self.__raven_count = raven_count
        self.__choice_selection = choice_selection
        self.reset()

    def reset(self):
        self._trees = dict([(obst, self.__obst_count) for obst in self.__obst])
        self._raven = self.__raven_count
        self._last_dice = None


    def play(self):
        """
        Simulates a full round of play, including taking the optimal choices
        @return: True if Players win, False if Players loose
        """
        
        self.reset()

        game_result = None

        while game_result == None:

            # Check loose/win conditions
            game_result = self.play_single_round()
        
        return game_result
    
    def play_single_round(self):
        """
        Plays a single round.
        @return: None: Game not ended
                 True: Players Win
                 False: Player Looses
        """
        self._roll_dice()
        return self._check_end_condition()

    def _check_end_condition(self):
        if self._raven <= 0:
            return False

        if sum(self._trees.values()) <= 0:
            return True
        
        return None

    def _roll_dice(self):

        dice = random.choice(self.__dice)
        self._last_dice = dice

        if dice in self._trees:
            self._trees[dice] = max(0, self._trees[dice] - 1)
            return 

        if dice == self.__dice_badguy:
            self._raven -= 1
            return 
        
        if dice == self.__dice_choice:
            for _ in range(self.__choice_selection):
                # we freely can choose from the existing trees. Strategy: take the one with the most entries
                max_tree_item = max(self._trees.items(), key=lambda tree_item: tree_item[1])
                self._trees[max_tree_item[0]] = max(0, self._trees[max_tree_item[0]] - 1)
                return 
    
    def __str__(self):
        s = f"Würfel      : {self._last_dice}\n"
        s += "\n".join([f"{obst[0]:12s}: {obst[1]*'O'}" for obst in self._trees.items()])
        s += f"\n{self.__dice_badguy:12s}: {self._raven * 'X'}"
        return s


def simulate(rounds_count = 10000, obst_count = 4, raven_count = 6, choice_count = 1):
    game = Obstgarten()

    win_count = 0

    for _ in range(rounds_count):
        if game.play():
            win_count += 1

    return win_count / rounds_count

def single_game():
    game = Obstgarten()

    round = 0
    game_end = None

    while game_end == None:
        round += 1
        game_end = game.play_single_round()
        print("==========================")
        print(f"Runde {round}")
        print(game)
    

def main():
    single_game()

    print(f"Win percenate classic: {simulate(10000)}")
    print(f"Win percenate new    : {simulate(10000, 10, 10, 2)}")

if __name__ == "__main__": main()
#EOF