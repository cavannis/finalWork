from abc import ABC, abstractmethod
"""this is the interface for species. so far it has three abstrac methods
one to get modifiers, one to get height, and one to return animosity"""
class SpeciesInt(ABC):

    @abstractmethod
    def getModifiers(self):
        """ return the species bonus for character stats
        """
        pass

    @abstractmethod
    def getHeight(self):
        """ return the height of the character"""
        pass

    @abstractmethod
    def returnAnimosity(self, otherSpecies):

        """ returns how friendly or not to another species
        """
        pass



