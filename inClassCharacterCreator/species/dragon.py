from speciesInterface import SpeciesInt 
"""this is the dragon class file. It utilizes the three
methods from the speciesinterface"""
class Dragon(SpeciesInt):

    def getModifiers(self): 
        """gets the int stat modifiers for the dragon class"""
        statMods = { "strength": 8
                   , "dexterity": 5
                   , "magic": 7
                   }
        return statMods
    def getHeight(self):
        height = 6.6
        """gets the double height modifier for dragon class
        The height is countd in feet"""
        return height
    def returnAnimosity(self, otherSpecies):
        dwarf = 4
        """returns the friendlyness that the dragon class has towards otherspecies"""
        return dwarf