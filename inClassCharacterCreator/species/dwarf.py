from speciesInterface import SpeciesInt
"""this is the dwarf class file. It utilizes the three
methods from the speciesinterface"""
class Dwarf(SpeciesInt):
    
    def getModifiers(self):
        """ returns the int stat modifiers for the dwarf class"""
        statMods = { "strength": 4
                   , "dexterity": -2
                   , "magic": 3
                   }
        return statMods

    def getHeight(self):
        Height = 4.4
        """ returns the double height value for the dwarf class
        the height is counted in feet"""
        return Height
    
    def returnAnimosity(self, otherSpecies):
        dragon = 4
        """returns the friendlyness that the dwarf class has towards otherspecies
        this is out of a range of 0-10"""
        return dragon
        
