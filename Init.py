# -*- coding: utf-8 -*-
import json
from ChampionStats import ChampionStats
from Switch import itemStat

def readJson(url):
    with open(url) as json_file:
        data = json.load(json_file)
        print(data["data"]["Kaisa"]["stats"])
        

    
    
if __name__ == "__main__":
# =============================================================================
#     o = ChampionStats("dragontail-10.7.1/10.7.1/data/en_US/champion/Kaisa.json","Kaisa")
#     print(o.hp)
#     o.calculateStatsByLevel(18)   
#     print(o.totalHP)
#     o.addStats(10,0,0,0,0,0,0,0,0,0)        
#     print(o.totalHP)
#     o.calculateDPS(100)
# =============================================================================
    
    tags = set()
    statsKeys = set()
    with open("dragontail-10.7.1/10.7.1/data/en_US/item.json") as json_file:
            for obj in json.load(json_file)["data"].values():    
                for t in obj["tags"]:
                    tags.add(t)
    with open("dragontail-10.7.1/10.7.1/data/en_US/item.json") as json_file:
            for obj in json.load(json_file)["data"].values():    
                for t in obj["stats"]:
                    statsKeys.add(t)
    print("Tags:")
    print(tags)
    print("StatsKeys:")
    print(statsKeys)
    print(itemStat("ataciasicasi"))
    print(itemStat("FlatHPRegenMod"))
