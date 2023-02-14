import json as js
import random as rnd
import inquirer as inq
import platform as plf
import os
import time
import math
from saving import Saving

MAX_DATA = 30 # For example: cars.json have 150 cars, It's a lot, So MAX_DATA is sets how many objects Start.generate() can return
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
    def __init__(self, name, defWork):
        self.name = name
        self.rep = rnd.randint(15, 20)
        self.money = rnd.randint(500, 2000)
        #self.money = 9999999999
        self.age = rnd.randint(21, 35)
        self.hp = rnd.randint(1, 15)
        self.day = 0
        self.workexp = rnd.randint(0, 10)
        self.workBonusLevel = 2
        self.owned = {"cars": [], "phones": [], "houses": []}
        self.ownedValue = 0
        self.workcycle = 0
        self.billcycle = 0
        self.agecycle = 0
        self.bonuscycle = 0
        self.deathchance = 0
        if len(defWork) != 0:
            self.works = []
            for work in defWork:
                self.works.append(work)
            self.work = defWork[self.works[rnd.randint(0, len(self.works) - 1)]]
        else:
            self.work = defWork
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
    def __init__(self, player, world):
        self.player = player
        self.world = world

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    def Menu(self, player):
        while True:
            Game.clear()
            print(f"{player.name} ->\nMoney: {player.money}$, Reputation: {player.rep}, Age: {player.age}, Health: {player.hp}, Day: {player.day}")
            menuChoices = ["Buy Phones", "Buy Cars", "Buy Houses", "View Owned", "Donate", "Visit Hospital", "Change Work", "Sleep", "Save", "Exit"]
            questions = [
                inq.List(carousel=True, name = "Choice", message="What to do",
                choices=menuChoices,),]
            answers = inq.prompt(questions)
            if answers["Choice"] == "Exit":
                os.system('cls' if os.name == 'nt' else 'clear')
                quit()
            elif answers["Choice"] == "Save":
                Saving.save(player, "TestSave")
            elif answers["Choice"] == "Buy Cars":
                Game.buy("cars", self.player, self.world)
            elif answers["Choice"] == "Buy Phones":
                Game.buy("phones", self.player, self.world)
            elif answers["Choice"] == "Buy Houses":
                Game.buy("houses", self.player, self.world)
            elif answers["Choice"] == "View Owned":
                Game.viewOwned(self.player)
            elif answers["Choice"] == "Visit Hospital":
                Game.hospital(self.player)
            elif answers["Choice"] == "Sleep":
                Game.nextDay(self.player)
    def changeWork():
        pass
    def eventChooser(datafile):
        with open(datafile, "r") as outfile:
            data = js.load(outfile)
            for event in data:
                event = data[event]
        outfile.close()
        return rnd.choice(list(data.items()))
    def buy(type, player, world):
        Game.clear()
        if len(world.reference[type]) != 0:
            questions = [
                inq.List(carousel=True, name = "item", message="Buy",
                choices=world.reference[type]),]
            print(f"=Buy {type.capitalize()}=")
            answers = inq.prompt(questions)
            price = world.worldData[type][world.reference[type][answers["item"]]]["price"]
            print(answers["item"].strip() + ", Costs " + str(world.worldData[type][world.reference[type][answers["item"]]]["price"]) + "$")
            if player.money < price:
                print("Not Enough money!\n")
                time.sleep(2)
            else:
                buyOk = inq.confirm("Do you want to buy that?", default=False)
                if buyOk:
                    player.ownedValue += price
                    player.owned[type].append(answers["item"])
                    player.money -= price
                    player.rep -= world.worldData[type][world.reference[type][answers["item"]]]["rep"]
                    world.reference[type].pop(answers["item"])
                    if player.rep < 0:
                        player.rep = 0
                    print("Bought successfully!")
                    time.sleep(2)
        else:
            print(f"=Buy {type.capitalize()}=")
            print(f"No avaible {type.capitalize()}!")
            time.sleep(2)
    def viewOwned(player):
        Game.clear()
        print("=Owned=")
        print(f"Owned Value: {player.ownedValue}$")
        for category in player.owned:
            print(f"={category.capitalize()}=")
            for item in player.owned[category]:
                print("  " + item)
        input("<-Back")
    def hospital(player):
        Game.clear()
        print("=Hospital=")
        if player.hp == 15:
            print("No need to visit hospital!")
            time.sleep(2)
        else:
            questions = [
                inq.List(carousel=True, name = "heal", message="Heal",
                choices=["5HP", "10HP", "15HP"]),]
            answers = inq.prompt(questions)
            if answers["heal"] == "5HP":
                price = 50
                heal = 5
            elif answers["heal"] == "10HP":
                price = 120
                heal = 10
            elif answers["heal"] == "15HP":
                price = 200
                heal = 15
            if player.money < price:
                print("Not Enough money!")
                time.sleep(2)
            else:
                buyOk = inq.confirm(f"Do you want to buy some medicine ({price}$)?", default=False)
                if buyOk:
                    player.hp += heal
                    if player.hp > 15:
                        player.hp = 15
                    player.money -= price
                    print("Bought successfully!")
                    time.sleep(2)

    def work(player):
        salary =  rnd.randint(math.ceil(player.work["salary"] - player.work["salary"]/8), math.ceil(player.work["salary"] + player.work["salary"]/8))
        bonus = player.workBonusLevel * player.work["bonus"]
        player.money += salary + bonus
        Game.clear()
        print("=Work=")
        print(f"Today's salary is {salary}$")
        chance = rnd.randint(1, 10)
        if chance >= 6:
            if player.rep < 5:
                event = Game.eventChooser(f"Data{separator}lowrepevents.json")[1]
            else:
                event = Game.eventChooser(f"Data{separator}events.json")[1]
            print(event["description"])
            values = {"hp": "Health", "money": "Money", "rep": "Reputation"}
            print(values[event["type"]], "\n", event["result"])
            match event["type"]:
                case "hp":
                    player.hp = round(eval(str(player.hp) + event["result"]))
                    if player.hp > 15:
                        player.hp = 15
                    elif player.hp < 0:
                        player.hp = 0
                case "money":
                    player.money = round(eval(str(player.money) + event["result"]))
                    if player.money < 0:
                        player.money = 0
                case "rep":
                    player.rep = round(eval(str(player.rep) + event["result"]))
                    if player.rep > 20:
                        player.rep = 20
                    elif player.rep < 0:
                        player.rep = 0

        input("Press enter to continue...")

    def nextDay(player):
        Game.clear()
        print("Sleeping...")
        time.sleep(2)
        player.day += 1
        Game.work(player)

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
        self.thingsNames = ["cars", "phones", "houses", "works", "donate"]
        self.worldData = {}
        self.reference = {"cars": {}, "phones": {}, "houses": {}, "works": {}, "donate": {}}
        for thing in self.things:
            self.worldData[self.thingsNames[self.i]] = thing
            for entry in thing:
                self.refThing = entry
                self.refChange = self.reference.get(self.thingsNames[self.i])
                self.refChange[thing[entry]["name"]] = self.refThing
            if self.i != len(self.thingsNames) - 1:
                self.i += 1
