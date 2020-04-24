# -*- coding: utf-8 -*-
import json

class ChampionStats(object):    
    def __init__(self,url):
        self.hp = 0
        self.hpperlevel= 0
        self.mp = 0
        self.mpperlevel = 0
        self.movespeed = 0
        self.armor = 0
        self.armorperlevel = 0
        self.spellblock = 0
        self.spellblockperlevel = 0
        self.attackrange = 0
        self.hpregen = 0
        self.hpregenperlevel = 0
        self.mpregen = 0
        self.mpregenperlevel = 0
        self.crit = 0
        self.critperlevel = 0
        self.attackdamage = 0
        self.attackdamageperlevel = 0
        self.attackspeedperlevel = 0
        self.attackspeed = 0    
        self.totalHP=0
        self.totalMp=0
        self.totalArmor=0
        self.totalSpellblock=0
        self.totalHpregen=0
        self.totalmpRegen=0
        self.totalCrit=0
        self.totalAtackdamage=0
        self.totalAtackspeed=0
        self.armorPenetration=0
        self.create(url)
        
    def create(self,url,champion):
        with open(url) as json_file:
            stats = json.load(json_file)["data"][champion]["stats"]
            self.hp = stats['hp']
            self.hpperlevel= stats['hpperlevel']
            self.mp = stats['mp']
            self.mpperlevel = stats['mpperlevel']
            self.movespeed = stats['movespeed']
            self.armor = stats['armor']
            self.armorperlevel = stats['armorperlevel']
            self.spellblock = stats['spellblock']
            self.spellblockperlevel = stats['spellblockperlevel']
            self.attackrange = stats['attackrange']
            self.hpregen = stats['hpregen']
            self.hpregenperlevel = stats['hpregenperlevel']
            self.mpregen = stats['mpregen']
            self.mpregenperlevel = stats['mpregenperlevel']
            self.crit = stats['crit']
            self.critperlevel = stats['critperlevel']
            self.attackdamage = stats['attackdamage']
            self.attackdamageperlevel = stats['attackdamageperlevel']
            self.attackspeedperlevel = stats['attackspeedperlevel']
            self.attackspeed = stats['attackspeed']
        
    def calculateStatsByLevel(self,lvl):
        self.totalHP=self.hp+(lvl-1)*self.hpperlevel
        self.totalMp=self.mp+(lvl-1)*self.mpperlevel
        self.totalArmor=self.armor+(lvl-1)*self.armorperlevel
        self.totalSpellblock=self.spellblock+(lvl-1)*self.spellblockperlevel
        self.totalHpregen=self.hpregen+(lvl-1)*self.hpregenperlevel
        self.totalmpRegen=self.mpregen+(lvl-1)*self.mpregenperlevel
        self.totalCrit=self.crit+(lvl-1)*self.critperlevel
        self.totalAtackdamage=self.attackdamage+(lvl-1)*self.attackdamageperlevel
        self.totalAtackspeed=self.attackspeed*(1+lvl*self.attackspeedperlevel)
        
    def addStats(self,hp,mp,armor,sb,hpr,mpr,crit,ad,ats,armp):        
        self.totalHP+=hp
        self.totalMp+=mp
        self.totalArmor+=armor
        self.totalSpellblock+=sb
        self.totalHpregen+=hpr
        self.totalmpRegen+=mpr
        self.totalCrit+=crit
        self.totalAtackdamage+=ad
        self.totalAtackspeed+=ats
        self.armorPenetration+=armp
    
    def calculateDPS(self, targetArmor):
        dps = self.totalAtackdamage*self.totalAtackspeed*(1+self.totalCrit)*100/((targetArmor*(1-self.armorPenetration))+100)
        print(dps)
        
    
