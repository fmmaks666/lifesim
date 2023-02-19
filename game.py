import json as js
import random as rnd
import inquirer as inq
import platform as plf
import os
import time
import math
from saving import Saving


MAX_CYCLE = {
    "workcycle": 4,
    "billcycle": 6,
    "agecycle": 12,
    "bonuscycle": 2
}


separator = "/"
if plf.system() == "Windows":
    separator = "\\"

# TODO: Finish Project!!
# TODO: Make better balance
# OPTIMIZE: Shops, Work, Donate: Get Rid of "Reference Lists", Transfer some if .. else to match .. case
# FIXME: Current Reputation bonus (Donate To) is very unbalanced, so it need to be balanced

class Player:
    def __init__(self, name, defWork):
        self.name = name
        self.rep = rnd.randint(35, 50)
        self.money = rnd.randint(500, 2000)
        #elf.money = 99999999999999999
        self.age = rnd.randint(21, 35)
        self.hp = rnd.randint(1, 30)
        self.day = 0
        self.workexp = rnd.randint(0, 10)
        self.workBonusLevel = 0
        self.owned = {"cars": [], "phones": [], "houses": []}
        self.cycles = {
            "workcycle": 0,
            "billcycle": 0,
            "agecycle": 0,
            "bonuscycle": 0,
        }
        self.deathchance = 0
        self.ownedValue = 0
        self.dead = False
        self.ended = False
        self.deathReason = ""
        self.vistedHospital = False
        self.changedWork = False
        self.donated = False
        self.savingFirstTime = True
        if len(defWork) != 0:
            self.works = []
            for work in defWork:
                self.works.append(work)
            self.work = defWork[self.works[rnd.randint(0, len(self.works) - 1)]]
        else:
            self.work = defWork
class Start:
        # Donate To: Reputation Formula: Reputation*(Money/10000)*ReputationBonus
    def generateNoLimit():
        with open(datafile, "r") as outfile:
            data = js.load(outfile)
            outfile.close()
        return data
    def generate(datafile):
            with open(datafile, "r") as outfile:
                data = js.load(outfile)
                outfile.close()
            return data
class Game:
    def __init__(self, player, world):
        self.player = player
        self.world = world
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    def Menu(self, player):
        while True:
            Game.clear()
            isDead = Game.lifeCheck(self.player)
            if not isDead:
                isDead = Game.ageDeath(self.player)
            if isDead:
                return
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
            elif answers["Choice"] == "Change Work":
                Game.changeWork(self.player, self.world)
            elif answers["Choice"] == "Donate":
                Game.donate(self.player, self.world)
    def addCycle(player, type):
        cycle = player.cycles[type]
        maxValue = MAX_CYCLE[type]
        if cycle == maxValue:
            match type:
                case "agecycle":
                    player.age += 1
                    player.rep -= rnd.randint(1, 5)
                    if player.age >= 65:
                        player.deathchance += rnd.randint(1, 3)
                    if player.deathchance >= 99:
                        player.deathchance == 99
                    player.cycles[type] = 0
                    return True
                case "bonuscycle":
                    player.workBonusLevel += 1
                    player.cycles[type] = 0
                    return True
                case "workcycle":
                    player.workexp += 1
                    player.cycles[type] = 0
                    return True
                case "billcycle":
                    player.cycles[type] = 0
                    return rnd.randint(100, 250)
        else:
            player.cycles[type] += 1
            return False
    def lifeCheck(player, fromAge = False):
        war = rnd.randint(1, 1000)
        if war == 666:
            player.deathReason = "Nuclear Warfare just started, You were killed by Explosion"
            player.dead = True
            return player.dead
        if fromAge:
            player.deathReason = "Age. We hope Your life was Successful!"
            player.dead = True
            return player.dead
        if player.hp <= 0:
            player.deathReason = "Something went wrong with Your Health."
            player.dead = True
            return player.dead
        if player.rep <= 0:
            player.deathReason = "People disrespected You."
            player.ended = True
            return player.ended
        if player.money <= 0:
            player.deathReason = "You don't have any money to live."
            player.ended = True
            return player.ended
        return False
    def donate(player, world):
        Game.clear()
        print("=Donate=")
        if player.donated:
            print("You can't donate 2 times")
            return time.sleep(2)
        if player.money == 0:
            print("You don't have money")
            return time.sleep(2)
        if len(world.reference["donate"]) != 0:
            choices = world.reference["donate"]
            choices["Not Now"] = "close"
            questions = [
            inq.List(carousel=True, name = "item", message="Apply to",
            choices=choices),]
            answers = inq.prompt(questions)
            del world.reference["donate"]["Not Now"]
            if answers["item"] == "Not Now":
                return
            company =  world.worldData["donate"][world.reference["donate"][answers["item"]]]
            name = company["name"]
            doDonation = inq.confirm(f"Donate to {name}?", default=False)
            if not doDonation:
                print("You canceled Donation")
                return time.sleep(2)
            validAmount = False
            while not validAmount:
                money = [inq.Text("amount", message = "How many to donate?")]
                money = inq.prompt(money)
                if money["amount"].isdigit():
                    validAmount = True
                else:
                    print("Enter valid Amount!")
            if (player.money - int(money["amount"])) < 0:
                print("You don't have enough money!")
                return time.sleep(2)
            player.money -= abs(round((int(money["amount"]))))
            player.money
            if company["goodrep"]:
                player.rep += math.ceil(player.rep*(int(money["amount"])/10000)*company["repbonus"])
            else:
                player.rep -= math.ceil(player.rep*(int(money["amount"])/10000)*company["repbonus"])
            if player.rep > 50:
                player.rep = 50
            print("Donated Successful")
            player.donated = True
            time.sleep(2)
    def ageDeath(player):
        if player.age >= 65:
            chance = rnd.randint(0, 100)
            if chance < player.deathchance:
                return Game.lifeCheck(player, True)
    def changeWork(player, world):
        Game.clear()
        print("=Change Work=")
        if len(world.reference["works"]) != 0:
            name = player.work["name"]
            salary = player.work["salary"]
            if player.work["bonus"] <= 0:
                bonus = ", without bonuses."
            else:
                bonus = ", with bonuses."
            if player.changedWork:
                return input("You can't change work 2 times, Press enter to continue...")
            print(f"I'm working at {name}, Averange salary is {salary}${bonus} My work experience is {player.workexp}")
            choices = world.reference["works"]
            choices["Not Now"] = "close"
            questions = [
            inq.List(carousel=True, name = "item", message="Apply to",
            choices=choices),]
            answers = inq.prompt(questions)
            del world.reference["works"]["Not Now"]
            if answers["item"] == "Not Now":
                return
            newWork = world.worldData["works"][world.reference["works"][answers["item"]]]
            newName = newWork["name"]
            newSalary = newWork["salary"]
            newBonus = newWork["bonus"]
            if newWork["bonus"] <= 0:
                newBonusText = ", without bonuses."
            else:
                newBonusText = ", with bonuses."
            print(f"Work at {newName}, Averange salary: {newSalary}${newBonusText}")
            inq.confirm(f"Apply to {newName}?", default=True)
            if name == newName:
                print("I'm already working here")
                return time.sleep(2)
            if player.workexp < newWork["workexp"]:
                print("Not enough work experience!\n")
                return time.sleep(2)
            player.work["name"] = newName
            player.work["salary"] = int(newSalary)
            player.work["bonus"] = int(newBonus)
            player.workBonusLevel = 0
            print(f"Now You working at {newName}!")
            player.changedWork = True
            return time.sleep(2)
    def eventChooser(datafile):
        with open(datafile, "r") as outfile:
            data = js.load(outfile)
        outfile.close()
        return rnd.choice(list(data.items()))
    def buy(type, player, world):
        Game.clear()
        if len(world.reference[type]) != 0:
            choices = world.reference[type]
            choices["Not Now"] = "close"
            questions = [
                inq.List(carousel=True, name = "item", message="Buy",
                choices=choices),]
            print(f"=Buy {type.capitalize()}=")
            answers = inq.prompt(questions)
            del world.reference[type]["Not Now"]
            if answers["item"] == "Not Now":
                return
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
        if player.vistedHospital:
            print("You can't visit Hospital 2 times!")
            return time.sleep(2)
        if player.hp == 30:
            print("No need to visit hospital!")
            time.sleep(2)
        else:
            questions = [
                inq.List(carousel=True, name = "heal", message="Heal",
                choices=["5HP", "10HP", "15HP", "20HP","25HP","30HP", "Not Now"]),]
            answers = inq.prompt(questions)
            if answers["heal"] == "Not Now":
                return
            if answers["heal"] == "5HP":
                price = 50
                heal = 5
            elif answers["heal"] == "10HP":
                price = 120
                heal = 10
            elif answers["heal"] == "15HP":
                price = 200
                heal = 15
            elif answers["heal"] == "20HP":
                price = 300
                heal = 20
            elif answers["heal"] == "25HP":
                price = 450
                heal = 25
            elif answers["heal"] == "30HP":
                price = 600
                heal = 30
            if player.money < price:
                print("Not Enough money!")
                time.sleep(2)
            else:
                buyOk = inq.confirm(f"Do you want to buy some medicine ({price}$)?", default=False)
                if buyOk:
                    player.hp += heal
                    if player.hp > 30:
                        player.hp = 30
                    player.money -= price
                    print("Bought successfully!")
                    player.vistedHospital = True
                    time.sleep(2)

    def work(player):
        player.vistedHospital = False
        player.changedWork = False
        player.donated = False
        salary =  rnd.randint(math.ceil(player.work["salary"] - player.work["salary"]/8), math.ceil(player.work["salary"] + player.work["salary"]/8))
        bonus = player.workBonusLevel * player.work["bonus"]
        player.money += salary + bonus
        Game.clear()
        print("=Work=")
        print(f"Today's salary is {salary}$")
        chance = rnd.randint(1, 10)
        if chance >= 6:
            if player.rep <= 25:
                event = Game.eventChooser(f"Data{separator}lowrepevents.json")[1]
            else:
                event = Game.eventChooser(f"Data{separator}events.json")[1]
            print(event["description"])
            values = {"hp": "Health", "money": "Money", "rep": "Reputation"}
            what = values[event["type"]]
            print(values[event["type"]], "\n", event["result"])
            match event["type"]:
                case "hp":
                    player.hp = round(eval(str(player.hp) + event["result"]))
                    if player.hp > 30:
                        player.hp = 30
                    elif player.hp < 0:
                        player.hp = 0
                case "money":
                    player.money = round(eval(str(player.money) + event["result"]))
                    if player.money < 0:
                        player.money = 0
                case "rep":
                    player.rep = round(eval(str(player.rep) + event["result"]))
                    if player.rep > 50:
                        player.rep = 50
                    elif player.rep < 0:
                        player.rep = 0
        needFood = rnd.randint(1, 10)
        if needFood >= 5:
            foodPrice = rnd.randint(50, 150)
            print(f"Today You were neened to buy some food, that costed {foodPrice}$")
            player.money -= foodPrice
            if player.money < 0:
                player.money = 0
        for i in ["agecycle", "workcycle", "bonuscycle"]:
            Game.addCycle(player, i)
        bills = Game.addCycle(player, "billcycle")
        if type(bills) == int:
            print(f"Today I was neened to pay Bills, that was Cost {bills}$")
            player.money -= bills
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
