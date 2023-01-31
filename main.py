#!/bin/python3
import random as rnd
import json as js
import platform as plf
from saving import Saving
from game import Player, World, Game, Start

separator = "/"
if plf.system() == "Windows":
    separator = "\\"

def main():
    print("Welcome! This is LifeSim by fmmaks. Type character name to start!")
    loadsave = input("Do You want to load saved game? (y/N) ").lower()
    if loadsave == "y" or loadsave == "yes":
        Saving.load()
    else:
        playerName = input("Enter character name[>} ")
        if playerName == "" or playerName == " ":
            playerName = "BadBoy"
        player = Player(playerName)
    world = World(Start.generate(f"Data{separator}cars.json"), Start.generate(f"Data{separator}phones.json"), Start.generate(f"Data{separator}houses.json"), Start.generate(f"Data{separator}works.json"), Start.generate(f"Data{separator}defaultwork.json"), Start.generate(f"Data{separator}donateto.json"))
    play = Game(player, world)
    play.Menu(player)


# Entry point
if __name__ == "__main__":
    main()
else:
    raise Exception("You can't use main.py as module")
