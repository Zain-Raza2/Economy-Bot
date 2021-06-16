from Utilities.DataManager import data
from Utilities.DataManager import people
from Utilities.DataManager import saveData
from Models.Person import Person

def getPeople():
    return people

## People ##
def getPersonByID(personID):
    for person in people:
        if person.personID == personID:
            return person

def addPersonByID(newPersonID):
    template = {"PersonID": newPersonID, "Balance": 420, "XP": 0}

    data.append(template)
    saveData()
    people.append(Person(template))

## Balance ##
def addBalanceToPerson(person, newBalance):
    person.addBalance(newBalance)
    saveData()

def removeBalanceFromPerson(person, newDeduction):
    person.removeBalance(newDeduction)
    saveData()

def setBalanceToPerson(person, setBalance):
    person.setBalance(setBalance)
    saveData()

def isPaymentValid(balance, PaymentAmount):
    if PaymentAmount < int(balance) and PaymentAmount > 0:
        return True

## XP ##
def addXPToPerson(person, newXP):
    person.addXP(newXP)
    saveData()

def removeFromPersonXP(person, deductedXP):
    person.removeXP(deductedXP)
    saveData()

def setXPToPerson(person, setXP):
    person.setXP(setXP)
    saveData()