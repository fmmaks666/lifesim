#!/bin/python3
import random as rnd
import json as js
import inquirer as inq
import platform as plf
from saving import Saving
from game import Player, World, Game, Start

separator = "/"
if plf.system() == "Windows":
    separator = "\\"

def main():
    print("Welcome! This is LifeSim by fmmaks.")
    loadsave = input("Do You want to load saved game? (y/N) ").lower()
    if loadsave == "y" or loadsave == "yes":
        Saving.load()
    else:
        playerName = input("Enter character name[>} ")
        if playerName == "" or playerName == " ":
            playerName = "BadBoy"
        world = World(Start.generate(f"Data{separator}cars.json"), Start.generate(f"Data{separator}phones.json"), Start.generate(f"Data{separator}houses.json"), Start.generate(f"Data{separator}works.json"), Start.generate(f"Data{separator}defaultwork.json"), Start.generate(f"Data{separator}donateto.json"))
        player = Player(playerName, world.defWork)
        play = Game(player, world)
        play.Menu(player)
        if player.dead:
            print("You Died!")
        elif player.ended:
            print("Game Over!")
        print(f"Reason: {player.deathReason}")
        retry = inq.confirm("Would You to Retry?", default=False)
        if retry:
            Game.clear()
            main()
# Entry point
if __name__ == "__main__":
    main()
else:
    raise Exception("You can't use main.py as module")
