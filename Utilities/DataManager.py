import os
import json

from Models.Person import Person

with open("Storage\EconomyData.json") as file:
        data = json.load(file)
    
people = []
for personData in data:
    person = Person(personData)
    people.append(person)

def saveData():
    with open("Storage\EconomyData.json", "w") as file:
        json.dump(data, file)