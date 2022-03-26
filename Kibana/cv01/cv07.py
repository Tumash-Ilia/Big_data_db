from pprint import pprint

from elasticsearch import Elasticsearch

INDEX_NAME = 'person'


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


# Připojení k ES
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Kontrola zda existuje index 'person'
if not es.indices.exists(index=INDEX_NAME):
    # Vytvoření indexu
    es.indices.create(index=INDEX_NAME)

# Index není potřeba vytvářet - pokud neexistuje, tak se automaticky vytvoří při vložení prvního dokumentu


# 1. Vložte osobu se jménem John
def task_1():
    print_delimiter(1)
    doc = {
        "name": "John"
    }
    res = es.index(index=INDEX_NAME, id=111, body=doc)
    pprint(res)


# 2. Vypište vytvořenou osobu (pomocí get a parametru id)
def task_2():
    print_delimiter(2)
    res = es.get(index=INDEX_NAME, id=111)
    pprint(res)


# 3. Vypište všechny osoby (pomocí search)
def task_3():
    print_delimiter(3)
    es.indices.refresh(index=INDEX_NAME )
    res = es.search(index=INDEX_NAME, body={"query":{"match_all":{}}})
    pprint(res['hits']['hits'])


# 4. Přejmenujte vytvořenou osobu na 'Jane'
def task_4():
    print_delimiter(4)
    doc = {
        "name": "Jane"
    }
    res = es.update(index=INDEX_NAME, id=111, body={"doc": doc})
    pprint(res)


# 5. Smažte vytvořenou osobu
def task_5():
    print_delimiter(5)
    res = es.delete(index=INDEX_NAME, id=111)
    pprint(res)


# 6. Smažte vytvořený index
def task_6():
    print_delimiter(6)
    res = es.indices.delete(index=INDEX_NAME)
    pprint(res)

if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_5()
    task_6()
