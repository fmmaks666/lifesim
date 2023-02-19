import json as js
import platform as plf

separator = "/"
if plf.system() == "Windows":
    separator = "\\"
class Saving:
    @staticmethod
    def save(player, saveName):
        saveData = {
            "name": player.name,
            "rep": player.rep,
            "money": player.money,
            "age": player.age,
            "hp": player.hp,
            "workexp": player.workexp
            }
        with open(f"Saves{separator}{saveName}.json", "w+") as outfile:
            outfile.write(js.dumps(saveData, indent = 4))
    @staticmethod
    def load():
        # TODO: Implement Loadings
        pass
