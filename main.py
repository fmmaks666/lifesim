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
    loadsave = inq.confirm("Do You want to load saved game?", default=False)
    if loadsave:
        saveName = [inq.Text("saveName", message = "Enter save name")]
        saveName = inq.prompt(saveName)
        if saveName["saveName"].strip() == "":
            quit("Enter valid Name!")
        loaded = Saving.load(saveName["saveName"])
        stats = loaded[0]
        worldLoaded = loaded[1]
        print(worldLoaded.keys())
        world = worldLoaded["worldData"]
        reference = worldLoaded["reference"]
        defaultwork = worldLoaded["defaultwork"]
        print(world, reference, defaultwork)
        world = World(world, reference, defaultwork)
    else:
        playerName = input("Enter character name[>} ")
        if playerName == "" or playerName == " ":
            playerName = "BadBoy"
        cars = Start.generate(f"Data{separator}cars.json")
        phones = Start.generate(f"Data{separator}phones.json")
        houses = Start.generate(f"Data{separator}houses.json")
        works = Start.generate(f"Data{separator}works.json")
        defaultwork = Start.generate(f"Data{separator}defaultwork.json")
        donateto = Start.generate(f"Data{separator}donateto.json")
        generatedWorldData = Start.generateWorldData(cars, phones, houses, works, donateto)
        generatedReference = Start.generateReference(cars, phones, houses, works, donateto)
        world = World(generatedWorldData, generatedReference, defaultwork)
        choosenWork = Start.chooseWork(world.defWork)
        stats = {
            "name": playerName,
            "rep": rnd.randint(35, 50),
            "money": rnd.randint(500, 2000),
            #"money": 99999999999999999,
            "age": rnd.randint(21, 35),
            "hp": rnd.randint(1, 30),
            "day": 0,
            "workexp": rnd.randint(0, 10),
            "workBonusLevel": 0,
            "owned": {"cars": [], "phones": [], "houses": []},
            "cycles": {
                "workcycle": 0,
                "billcycle": 0,
                "agecycle": 0,
                "bonuscycle": 0,
            },
            "work": choosenWork,
            "deathchance": 0,
            "ownedValue": 0,
            "vistedHospital": False,
            "changedWork": False,
            "donated": False,
            "customSaveName": False,
            "enableNuclearWar": False,
            "savingFirstTime": True
        }
    player = Player(stats)
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
