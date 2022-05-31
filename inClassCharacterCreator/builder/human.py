
class Human():

    def __init__(self):
        self.characterInfo = []

    def addToInfo(self, Info):
        self.characterInfo.append(Info)
    
    def ListCharacter(self):
        print(f"Character Info: { ', '.join(self.characterInfo)}", end="")