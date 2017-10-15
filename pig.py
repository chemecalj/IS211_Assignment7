#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS_211 Week 7, Assignment 1, Pig Game."""

import random
import textwrap

class dice():
    def __init__(self):
        self.value = 0
        seed = 0
    def roll(self):
        self.value = random.randint(1,6)

class Player():
    def __init__(self):
        self.turn = False
        self.roll = True
        self.hold = False
        self.score = 0

    def decide(self):
        decision = raw_input('Would you like to "Hold" or "Roll"? ')
        print
        decision = decision.lower()
        if decision == 'hold':
            self.hold = True
            self.roll = False
        elif decision == 'roll':
            self.hold = False
            self.roll = True
        else:
            print('Invalid choice, you must type "Hold" or "Roll". ')
            self.decide()

class Game():
    def __init__(self, player_1, player_2, die):
        self.turn_score = 0
        self.die = die
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1.score = 0
        self.player_2.score = 0
        self.player_1.name = "Player 1"
        self.player_2.name = "Player 2"

        print raw_input("Press enter to determine who will go first (Coin Toss). ")
        print
        flip_result = random.randint(1, 2)
        if flip_result == 1:
            self.current_player = player_1
            print "Player 1 wins the coin toss. "
            print
        elif flip_result == 2:
            self.current_player = player_2
            print "Player 2 wins the coin toss. "
            print
        self.turn()

    def next_turn(self):
        self.turn_score = 0
        if self.player_1.score >= 100:
            print "Player 1 wins! "
            print "Score:", self.player_1.score
            self.endgame()
            nextgame()
        elif self.player_2.score >= 100:
            print "Player 2 wins! "
            print "Score:", self.player_2.score
            self.endgame()
            nextgame()
        else:
            if self.current_player == self.player_1:
                self.current_player = self.player_2
            elif self.current_player == self.player_2:
                self.current_player = self.player_1
            print "Next turn, it is ", self.current_player.name, "'s turn. "
            print
            self.turn()

    def turn(self):
        self.die.roll()
        if (self.die.value == 1):
            print "You Rolled a 1! No points added, your turn is over. "
            print
            print "Player 1 Score: ", self.player_1.score
            print
            print "Player 2 Score: ", self.player_2.score
            print
            self.turn_score = 0
            self.next_turn()
        else:
            self.turn_score = self.turn_score + self.die.value
            print "You rolled a: ", self.die.value
            print
            print "Current Value is: ", self.turn_score
            print
            print "Player 1 Score: ", self.player_1.score
            print
            print "Player 2 Score: ", self.player_2.score
            print
            self.current_player.decide()
            if (self.current_player.hold == True and self.current_player.roll == False):
                self.current_player.score = self.current_player.score + self.turn_score
                self.next_turn()
            elif (self.current_player.hold == False and self.current_player.roll == True):
                self.turn()

    def endgame(self):
        self.player_1 = None
        self.player_2 = None
        self.die = None
        self.turn_score = None

def nextgame():
    new = raw_input('Welcome to the Pig Game. Read the rules, or start the game? ("Read" / "Start") ')
    if new.lower() == "read":
        print
        instructions = "The rules of Pig are simple. " \
                       "The game features two players, whose goal is to reach 100 points first. " \
                       "Each turn, a player repeatedly rolls a die until either a 1 is rolled " \
                       "or the player holds and scores the sum of the rolls (i.e. the turn total). At any time " \
                       "during a player's turn, the player is faced with two decisions: ROLL ­ If the player rolls " \
                       "a 1: the player scores nothing and it becomes the opponent's turn. If the player rolls 2 ­ 6:" \
                       " the number is added to the player's turn total and the player's turn continues. HOLD ­ The " \
                       "turn total is added to the player's score and it becomes the opponent's turn."
        print textwrap.fill(instructions, 36)
        print
        new = raw_input('Ready to start? Type, "Start" to begin!')
        print
    if new.lower() == "start":
        player_1 = Player()
        player_2 = Player()
        die = dice()
        newgame = Game(player_1, player_2, die)

if __name__ == '__main__':
    nextgame()
