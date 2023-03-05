"""
Author:     Calvin Henggeler
Project:    Exam 1
Course:     CS-399 Intermediate Python
Date:       2/23/2023

Disclaimers:
            No AI Tools were used to make this code

Description:
            Make an OOP that simulates the Chicago and Double-Roll Games

*** Thank you for letting us have more time to submit more completed code.***

Revision Notes:
    Nicely done! Still please consider the comments below:

    Dataclass exist to reduce redundant code like __init__ So ideally it would
    have been just:
        @dataclass
        Class Player:
            name: str
            score = 0

    In the champions implementation max(scores) gets calculated (1 + number of players) times .. that's wasteful.
    Why not store it in a variable instead? winning_score = max(scores) ... Or even tighter:
        winner = max(self.players, key = lambda p:p.score)
        return [p for p in self.players if p.score == winner.score] if winner.score > 0 else []

    You are using an unusual dice. Yours has seven faces ;-)
    To be true to the game, with those dice your target combinations should
    have been adjusted to 2,3,4,..,14. Good programmers don't repeat code:
    The beginning of both games' play method looks the same. This work should
    be done in the base class instead.

"""

# =========================================================================== #
#                                   Imports                                   #
# =========================================================================== #
from abc import ABC, abstractmethod
from dataclasses import dataclass
from random import randint


# =========================================================================== #
#                                   Classes                                   #
# =========================================================================== #

# ------------------------------- Player Class ------------------------------ #
@dataclass
class Player:
    name: str
    score = 0


# -------------------------------- Game Class ------------------------------- #
class Game(ABC):
    """
    Game baseclass. Chicago and DoubleRoll inherit from here
    """
    num_games_played = 0

    def __init__(self, players: [Player]) -> None:
        self.players = players      # make list of players
        self.champs = []            # init list of champs as empty

    def champions(self) -> [Player]:
        """
        :return: list of player(s), with the highest score, or an empty list,
                if nobody scored.
        """

        # form a list of the scores (LIST COMPREHENSION)
        scores = []
        [scores.append(_player.score) for _player in self.players]

        # if nobody scored, return empty list with no winners
        if max(scores) == 0:
            return []

        winner = max(self.players, key=lambda p: p.score)
        return [p for p in self.players if p.score == winner.score] if winner.score > 0 else []

        # # Filter player list for high scores, store is champs for later
        # max_score = max(scores)
        # self.champs = list(filter(lambda x: x.score == max_score, self.players))
        # return self.champs


    @abstractmethod
    def play(self) -> [Player]:
        """ Child classes must implement this """
        pass


# ------------------------------ Chicago Class ------------------------------ #
class Chicago(Game):
    """
    Model of the Chicago Dice Game
    """
    _rounds = range(1, 12)

    def __init__(self, players: [Player]) -> None:
        super().__init__(players)

    def play(self) -> [Player]:
        """
        Plays the game
        :return: List of winners using the champions method
        """
        # Increment the number of games played
        self.__class__.num_games_played += 1

        # Reset scores of all the players
        for _player in self.players:
            _player.score = 0

        # go through the rounds
        for round_num in self._rounds:

            # Each player gets a turn
            for _player in self.players:

                # Player rolls both dice
                turn_score = randint(1, 7) + randint(1, 7)

                # if the sum of the dice == target combination, add to player score
                if turn_score == round_num + 1:
                    _player.score += turn_score

        # use champions method to return list of winners
        return self.champions()


# ----------------------------- DoubleRoll Class ---------------------------- #
class DoubleRoll(Game):
    """
    Models the DoubleRoll Game, a variant of Chicago
    """
    _rounds = range(1, 12)

    def __init__(self, players: [Player]) -> None:
        super().__init__(players)

    def play(self) -> [Player]:
        """
        Plays the game
        :return: List of winners using the champions method
        """
        # Increment the number of games played
        self.__class__.num_games_played += 1

        # Reset scores of all the players
        for _ in self.players:
            _.score = 0

        # go through the rounds
        for round_num in self._rounds:

            # Each player gets a turn
            for _player in self.players:

                # Player rolls both dice
                die1 = randint(1, 7)
                die2 = randint(1, 7)
                turn_score = die1 + die2

                # if the sum of the dice == target combination, add to player score
                if turn_score == round_num + 1:
                    _player.score += turn_score
                else:  # This is the chance to re roll for points
                    # re-rolL one die
                    turn_score = die1 + randint(1, 6)
                    if turn_score == round_num + 1:
                        _player.score += turn_score

        # use champions method to return list of winners
        return self.champions()


# =========================================================================== #
#                              Execution/Test Code                            #
# =========================================================================== #
if __name__ == "__main__":

    # List of Contestants
    contestants = [
        Player("Ricky Bell"),
        Player("Michael Bivins"),
        Player("Bobby Brown"),
        Player("Ronnie DeVoe"),
        Player("Johnny Gill"),
        Player("Ralph Tresvant"),
        Player("Calvin Henggeler"),
        Player("Carl the Cat")
    ]

    # Play both games until there are more than 1 winner in each games
    for game in (Chicago(contestants), DoubleRoll(contestants)):
        while True:
            winners = game.play()               # play the game

            # Check for more than 1 winner
            if len(winners) > 1:
                print(f"\nAfter {game.num_games_played} games of {str(game.__class__.__name__)} played,"
                      f" a single game had multiple winners:")

                # Print the winners
                inline_str = "Winners: "
                for champ in game.champs:
                    inline_str += f"{champ.name}, Score: {champ.score}  "
                print(inline_str)

                # Show results of the game
                print("Game Results:")
                for player in game.players:
                    print(f"{player.name.ljust(25)} --> {player.score}")

                # break from the loop
                break
