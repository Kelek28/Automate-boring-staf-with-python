# Chapter 6
# Project: Zombie Dice Bots

import random
import zombiedice


class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # A bot that stops rolling after it has rolled two brains
        while diceRollResults is not None:
            randomNumber = random.randint(0, 1)
            if randomNumber == 1:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break
        # A bot that stops rolling after it has rolled two shotguns
        while diceRollResults is not None:
            randomNumber = random.randint(0, 1)
            if randomNumber == 1:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class stopAfterTwoShotGun(MyZombie):
    def __init__(self):
        self.name = "stopAfterTwoShotGun"

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll
        shotgun = 0
        # A bot that stops rolling after it has rolled two brains
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun == 2:
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again


class stopAfterTwoBrain(MyZombie):
    def __init__(self):
        self.name = "stopAfterTwoBrain"

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll
        brains = 0
        # A bot that stops rolling after it has rolled two brains
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains == 2:
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again


class stopAfterFirstRollRandom(MyZombie):
    def __init__(self):
        self.name = "stopAfterFirstRollRandom"

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll
        # A bot that, after the first roll, randomly decides if it will continue or stop
        while diceRollResults is not None:
            randomNumber = random.randint(0, 1)
            if randomNumber == 1:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class roll1to4times(MyZombie):
    def __init__(self):
        self.name = "roll1to4timesZombie"

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll
        shotguns = 0
        # A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
        for i in range(random.randint(1, 4)):
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class moreShotgunThanBrain(MyZombie):
    def __init__(self):
        self.name = "roll1to4timesZombie"

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll
        brains = 0
        shotguns = 0
        # A bot that stops rolling after it has rolled more shotguns than brains
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns < brains:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Stop at 1 Shotgun', minShotguns=1),
    stopAfterTwoShotGun(),
    stopAfterTwoBrain(),
    stopAfterFirstRollRandom(),
    roll1to4times(),
    moreShotgunThanBrain()

)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
