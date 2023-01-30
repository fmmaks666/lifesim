import json as js
import random as rnd
import inquirer as inq
import platform as plf
import os
from saving import Saving

MAX_DATA = 30 #For example: cars.json have 150 cars, It's a lot, So MAX_DATA is sets how many objects Start.generate() can add to shops
WORK_EXP_CYCLE = 3
BILLS_CYCLE = 6
AGE_CYCLE = 12
WORK_BONUS_CYCLE = 6

separator = "/"
if plf.system() == "Windows":
    separator = "\\"

# TODO: Finish Project!!
# TODO: Make better balance
# OPTIMIZE: Shops, Work, Donate: Get Rid of "Reference Lists"
# FIXME: Current Reputation bonus (Donate To) is very unbalanced, so it need to be balanced

class Player:
    def __init__(self, name):
        self.name = name
        self.rep = rnd.randint(15, 20)
        self.tired = False
        self.money = rnd.randint(500, 2000)
        self.age = rnd.randint(21, 35)
        self.hp = rnd.randint(1, 15)
        self.workexp = rnd.randint(0, 10)
class Start:
        # Donate To: Reputation Formula: (Money/Reputation)*ReputationBonus*10//5
    def generateNoLimit():
        with open(datafile, "r") as outfile:
            data = js.load(outfile)
            outfile.close()
        return data
    def generate(datafile):
            with open(datafile, "r") as outfile:
                data = js.load(outfile)
                outfile.close()
            if len(data) >= MAX_DATA:
                rnd.shuffle(data)
                return(data[:MAX_DATA])
            return data
class Game:
    def Menu(player):
        while True:
            print(f"{player.name} ->\nMoney: {player.money}$, Reputation: {player.rep}, Age: {player.age}, Health: {player.hp}")
            menuChoices = ["Buy Phones", "Buy Cars", "Buy Houses", "Owned", "Donate", "Visit Hospital", "Sleep", "Save", "Exit"]
            questions = [
                inq.List(carousel=True, name = "Choice", message="What to do",
                choices=menuChoices,),]
            answers = inq.prompt(questions)
            if answers["Choice"] == "Exit":
                os.system('cls' if os.name == 'nt' else 'clear')
                quit()
            if answers["Choice"] == "Save":
                Saving.save(player, "TestSave")
                with open(datafile, "r") as outfile:
                    data = js.load(outfile)
                    photo = data["photo"]
                    print(photo["description"])
                    outfile.close()

    def changeWork():
        pass
    def eventChooser(datafile):
        with open(datafile, "r") as outfile:
            data = js.load(outfile)
            print(len(data))
            for event in data:
                event = data[event]
                for info in event:
                    print(event[info])
        outfile.close()

class World:
    def __init__(self, cars, phones, houses, works, defWork, donate):
        self.cars = cars
        self.phones = phones
        self.houses = houses
        self.works = works
        self.defWork = defWork
        self.donate = donate
        # TEMP: Reference Lists, to be fixed
        self.things = [self.cars, self.phones, self.houses, self.works, self.donate]
        self.i = 0
        self.thingsNames = ["cars", "phones", "works", "donate"]
        self.reference = {"cars": "", "phones": "", "works": "", "donate": ""}
        print(self.reference[0])
        for thing in self.things:
            for entry in thing:
                thing.get(entry).get("name")
                self.i += 1
