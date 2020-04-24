# -*- coding: utf-8 -*-



def itemStat(stat):
    switcher={
            'FlatMovementSpeedMod':1,
            'FlatPhysicalDamageMod':2,
            'FlatHPPoolMod':3,
            'PercentMovementSpeedMod':4,
            'FlatCritChanceMod':5,
            'PercentLifeStealMod':6,
            'PercentAttackSpeedMod':7,
            'FlatArmorMod':8,
            'FlatMagicDamageMod':9,
            'FlatSpellBlockMod':10,
            'FlatMPPoolMod':11,
            'FlatHPRegenMod':12
            }
    return switcher.get(stat,"0")
