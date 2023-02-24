"""
Author: Calvin Henggerl
Assignment Exam 1: Make a program that simulates the Chicago and Douvle-Roll game
CS-399 Intermediate Python
2/23/2023

No AI was used to make this code
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint


class Dice:
    value: int

    def roll(self):
        self.value = randint(1, 7)
        return self.value


@dataclass
class Player:
    name: str

    def __init__(self, name: str):
        self.name = name    # set the player name
        self.score = 0      # init the player score to 0

    def __str__(self) -> str:
        return self.name


class Game(ABC):

    def __init__(self, players: [Player]) -> None:
        self.players = players      # make list of players
        self.champs = []            # init list of champs as empty
        self.dice1 = Dice()         # create Dice as attributes the game
        self.dice2 = Dice()

    def champions(self) -> [Player]:
        """:return: list of player(s), with the highest score, or an empty list, if nobody scored."""

        scores = []
        for player in self.players:
            scores.append(player.score)

        return filter(lambda x: x.score == max(scores), self.players )

    @abstractmethod
    def play(self) -> [Player]:
        """ Child Classes must implement this """
        pass


class Chicago(Game):

    _rounds = range(1, 12)
    num_games_played = 0

    def __init__(self, players: [Player]) -> None:
        super().__init__(players)
        self.__class__.num_games_played = 0

    def play(self) -> [Player]:

        # Increment the number of games played
        self.num_games_played += 1

        # go through the rounds
        for round_num in self._rounds:

            # Each player gets a turn
            for player in self.players:

                # Player rolls both dice
                turn_score = self.dice1.roll() + self.dice2.roll()

                # if the sum of the dice == target combination, add to player score
                if turn_score == round_num + 1:
                    player.score += turn_score

        # use champions method to return lit of winners
        return self.champions()


class DoubleRoll(Game):

    _rounds = range(1, 12)

    def __init__(self, players: [Player]) -> None:
        super().__init__(players)


    def play(self) -> [Player]:
        pass


if __name__ == "__main__":

    """Test Dice"""
    dice1 = Dice()
    for _ in range(1,7):
        print((dice1.roll()))
    print("Dice Test: Passed")


    contestants = [
        Player("Ricky Bell"),
        Player("Michael Bivins"),
        Player("Bobby Brown"),
        Player("Ronnie DeVoe"),
        Player("Johnny Gill"),
        Player("Ralph Tresvant")
    ]

    """ test sub class attributes"""
    chicago = Chicago(contestants)
    chicago.play()
    print(chicago.__dict__)

    for player in chicago.players:
        print(f"{player.name} with score {player.score}")

    double_roll = DoubleRoll(contestants)
    print(double_roll.__dict__)





    """
    for game in (Chicago(contestants), DoubleRoll(contestants)):
        while True:
            pass
            #winners = game.play()              # play the game
            #game_cahmps = game.champions()     # get the list of champions
                                                # print the list of Champions

    """