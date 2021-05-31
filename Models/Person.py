class Person():
    def __init__(self, personData):
        print(personData)
        self.data = personData
        self.personID = personData["PersonID"]
    ## BALANCE ##

    def getBalance(self):
        return self.data["Balance"]

    def setBalance(self, setBalance):
        self.data["Balance"] = setBalance

    def addBalance(self, newBalance):
        self.data["Balance"] += newBalance

    def removeBalance(self, newDeduction):
        self.data["Balance"] -= newDeduction

    ## XP ##

    def getXP(self):
        return self.data["XP"]

    def setXP(self, setXP):
        self.data["XP"] = setXP

    def addXP(self, newXP):
        self.data += newXP
    
    def removeXP(self, deductedXP):
        self.data -+ deductedXP
    