from builderInt import BuildterInt
from ages.age import Age
from human import Human
class HumanBuilder(BuildterInt):

    def __init__(self):
        self.reset()
    
    def reset(self):
        self._human = Human()
    
    def setAge(self) -> Age:
        self.charactername = Age()

        print("your character name is", self.charactername)
        return self.charactername
    


