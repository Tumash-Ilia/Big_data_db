"""
DPB - 5. Cvičení

Implementujte jednotlivé body pomocí PyMongo knihovny - rozhraní je téměř stejné jako v Mongo shellu.
Před testováním Vašich řešení si nezapomeňte zapnout Mongo v Dockeru.

Pro pomoc je možné např. použít https://www.w3schools.com/python/python_mongodb_getstarted.asp

Funkce find vrací kurzor - pro vypsání výsledku je potřeba pomocí foru iterovat nad kurzorem:

cursor = collection.find()
for restaurant in cursor:
    print(restaurant) # případně print(restaurant['name'])

Všechny výsledky limitujte na 10 záznamů. Nepoužívejte české názvy proměnných!
"""

import pprint
from datetime import datetime

import pymongo
from bson import ObjectId
from init import collection


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


# 1. Vypsání všech restaurací - pouze názvů, abecedně seřazených
def task_1():
    print_delimiter(1)
    for rest in collection.find({}, {"_id": 0, "name": 1}).sort("name", 1).limit(10):
        print(rest)


# 2. Zobrazte dalších 10 záznamů
def task_2():
    print_delimiter(2)
    for rest in collection.find({}, {"_id": 0, "name": 1}).sort("name", 1).skip(10).limit(10):
        print(rest)


# 3. #Vypsání restaurací ve čtvrti Bronx (čtvrť = borough)
def task_3():
    print_delimiter(3)
    for rest in collection.find({"borough": 'Bronx'}).limit(10):
        # pprint.pprint(rest)
        print(rest)


# 4. Vypsání restaurací, jejichž název začíná na písmeno M
def task_4():
    print_delimiter(4)
    for rest in collection.find({"name": {'$regex': '^M'}}, {"_id": 0, "name": 1}).limit(10):
        # pprint.pprint(rest)
        print(rest)


# 5. Vypsání restaurací, které mají skóre větší než 80
def task_5():
    print_delimiter(5)
    for rest in collection.find({"grades.score": {"$gt": 80}}).limit(10):
        # pprint.pprint(rest)
        print(rest)


# 6. Vypsání restaurací, které mají skóre mezi 80 a 90
def task_6():
    print_delimiter(6)
    for rest in collection.find({"grades.score": {"$elemMatch": {"$gt": 80, "$lt": 90}}}):
        # pprint.pprint(rest)
        print(rest)


'''
V této části budete opět vytvářet vlastní restauraci.

Řešení:
Vytvořte si vaši restauraci pomocí slovníku a poté ji vložte do DB.
restaurant = {
    
}
'''


# 7. Uložte novou restauraci (stačí vyplnit název a adresu)
def task_7(restaurant):
    print_delimiter(7)
    inserted = collection.insert_one(restaurant)
    print(inserted.inserted_id)


# 8. Vypište svoji restauraci
def task_8(name):
    print_delimiter(8)
    for rest in collection.find({"name": name}):
        pprint.pprint(rest)


# 9. Aktualizujte svoji restauraci - změňte libovolně název
def task_9():
    print_delimiter(9)
    collection.update_one({"name": 'Moris Park Bake Shop'}, {"$set": {"name": 'Moris Park'}})


# 10. Smažte svoji restauraci
# 10.1 pomocí id (delete_one)
def task_10a(id):
    print_delimiter(10)
    collection.delete_one({"_id": ObjectId(id)})


# 10.2 pomocí prvního nebo druhého názvu (delete_many, využití or)


def task_10b(name1, name2):
    print_delimiter(10)
    collection.delete_many({"$or": [{"name": name1}, {"name": name2}]})


'''
Poslední částí tohoto cvičení je vytvoření jednoduchého indexu.

Použijte např. 3. úlohu s vyhledáváním čtvrtě Bronx. První použijte Váš již vytvořený dotaz a na výsledek použijte:

cursor.explain()['executionStats'] - výsledek si vypište na výstup a všimněte si položky 'totalDocsExamined'

Poté vytvořte index na 'borough', zopakujte dotaz a porovnejte hodnoty 'totalDocsExamined'.

S řešením pomůže https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.create_index
'''


def task_11():
    print_delimiter(11)
    cursor1 = collection.find({"borough": 'Bronx'}).explain()['executionStats']
    collection.create_index([("borough", pymongo.DESCENDING)])
    cursor2 = collection.find({"borough": 'Bronx'}).explain()['executionStats']
    print(cursor1)
    print(cursor2)


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    restaurant = {
        "address": {
            "building": "97-22",
            "coord": [- 73.8601152, 40.7311739],
            "street": "63 Road",
            "zipcode": "11374"
        },
        "borough": "Queens",
        "cuisine": "Jewish/Kosher",
        "grades": [{
            "date": datetime.utcnow(),
            "grade": "Z",
            "score": 20
        }, {
            "date": datetime.utcnow(),
            "grade": "A",
            "score": 13
        }, {
            "date": datetime.utcnow(),
            "grade": "A",
            "score": 13
        }, {
            "date": datetime.utcnow(),
            "grade": "B",
            "score": 25
        }],
        "name": "Moris Park Bake Shop",
        "restaurant_id": "30075445"
    }
    task_7(restaurant)
    task_9()
    task_8('Moris Park')
    task_10a("605c9a762432229fb46609f6")
    task_8('Moris Park')
    task_10b('Moris Park', 'Moris Park Bake Shop')
    task_8('Moris Park')
    task_11()
