from init import collection
from bson.code import Code

'''
DPB - 6. cvičení - Agregační roura a Map-Reduce

V tomto cvičení si můžete vybrat, zda ho budete řešit v Mongo shellu nebo pomocí PyMongo knihovny.

Před testováním Vašich řešení si nezapomeňte zapnout Mongo v Dockeru - používáme stejná data jako v minulých cvičeních.

Pro pomoc je možné např. použít https://api.mongodb.com/python/current/examples/aggregation.html a přednášku.

Všechny výsledky limitujte na 10 záznamů. Nepoužívejte české názvy proměnných!

Struktura záznamu v db:
{
  "address": {
     "building": "1007",
     "coord": [ -73.856077, 40.848447 ],
     "street": "Morris Park Ave",
     "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
     { "date": { "$date": 1393804800000 }, "grade": "A", "score": 2 },
     { "date": { "$date": 1378857600000 }, "grade": "A", "score": 6 },
     { "date": { "$date": 1358985600000 }, "grade": "A", "score": 10 },
     { "date": { "$date": 1322006400000 }, "grade": "A", "score": 9 },
     { "date": { "$date": 1299715200000 }, "grade": "B", "score": 14 }
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
'''


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


'''
Agregační roura
Zjistěte počet restaurací pro každé PSČ (zipcode)
 a) seřaďte podle zipcode vzestupně
 b) seřaďte podle počtu restaurací sestupně
Výpis limitujte na 10 záznamů a k provedení použijte collection.aggregate(...)
'''


def task_1a():
    print_delimiter('1 a)')
    res = collection.aggregate([
        {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
        {"$limit": 10}
    ])
    for r in res:
        print(r)


def task_1b():
    print_delimiter('1 b)')
    res = collection.aggregate([
        {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for r in res:
        print(r)

'''
Agregační roura

Restaurace obsahují pole grades, kde jsou jednotlivá hodnocení. Vypište průměrné score pro každou hodnotu grade.
V agregaci vynechte grade pro hodnotu "Not Yet Graded" (místo A, B atd. se může vyskytovat tento řetězec).

'''


def task_2():
    print_delimiter(2)
    res = collection.aggregate([
        {"$match": {"grades.grade": {"$ne": "Not Yet Graded"}}},
        {"$unwind": "$grades"},
        {"$group": {"_id": "$grades.grade", "average_score": {"$avg": "$grades.score"}}},
        {"$sort": {"_id": 1}},
        {"$limit": 10}
    ])
    for r in res:
        print(r)

'''
Map-Reduce

Zadání je stejné jako u 1. příkladu pro agregační rouru - pouze realizovat přes Map-Reduce. 

Při řešení může pomoct:
https://pymongo.readthedocs.io/en/stable/examples/aggregation.html
https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.map_reduce 
'''


def task_3():
    print_delimiter(3)
    mapper = Code("""
                      function () {
                          emit(this.address.zipcode, 1);
                      }
                      """)
    reducer = Code("""
                        function (key, values) {
                        return Array.sum(values);
                        }
                      """)
    res = collection.map_reduce(mapper, reducer, "myresults")
    for r in res.find().sort("_id").limit(10):
        print(r)

'''
Map-Reduce

Zadání je stejné jako u 2. příkladu pro agregační rouru - pouze realizovat přes Map-Reduce.
'''


def task_4():
    print_delimiter(4)
    mapper = Code("""
                         function () {
                            for (var idx = 0; idx < this.grades.length; idx++){
                            var key = this.grades[idx].grade;
                            var value = this.grades[idx].score;
                            emit(key,value);
                            }
                         }
                         """)
    reducer = Code("""
                           function (key, values) {
                           return Array.avg(values);
                           }
                         """)
    res = collection.map_reduce(mapper, reducer, "myresults", query={"grades.grade": {"$ne": "Not Yet Graded"}})
    for r in res.find().sort("_id"):
        print(r)


if __name__ == '__main__':
    task_1a()
    task_1b()
    task_2()
    task_3()
    task_4()
