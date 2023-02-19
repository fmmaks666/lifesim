import json as js
import platform as plf
import pathlib as plib

separator = "/"
if plf.system() == "Windows":
    separator = "\\"
class Saving:
    @staticmethod
    def save(player, world, saveName):
        saveData = {
            "playerSave": {
                "name": player.name,
                "rep": player.rep,
                "money": player.money,
                #"money": 99999999999999999,
                "age": player.age,
                "hp": player.hp,
                "day": player.day,
                "workexp": player.workexp,
                "workBonusLevel": player.workBonusLevel,
                "owned": player.owned,
                "cycles": {
                    "workcycle": player.cycles["workcycle"],
                    "billcycle": player.cycles["billcycle"],
                    "agecycle": player.cycles["agecycle"],
                    "bonuscycle": player.cycles["bonuscycle"],
                },
                "work": player.work,
                "deathchance": player.deathchance,
                "ownedValue": player.ownedValue,
                "vistedHospital": player.vistedHospital,
                "changedWork": player.changedWork,
                "donated": player.donated,
                "customSaveName": player.customSaveName,
                "savingFirstTime": False
            },
            "worldSave":{
            "worldData": world.worldData,
            "reference": world.reference,
            "defaultwork": player.work
            }
        }
        with open(f"Saves{separator}{saveName}.json", "w+") as outfile:
            outfile.write(js.dumps(saveData, indent = 4))
    @staticmethod
    def load(saveName):
        saveFile = plib.Path(f"Saves{separator}{saveName}.json")
        if not saveFile.exists():
            quit("Save not Found!")
        with open(f"Saves{separator}{saveName}.json", "r") as outfile:
            loaded = js.load(outfile)
        return loaded["playerSave"], loaded["worldSave"]
