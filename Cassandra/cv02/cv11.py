from datetime import datetime

from cassandra.cluster import Cluster

'''
DPB - 11. cvičení Cassandra

Use case: Discord server - reálně používáno pro zprávy, zde pouze zjednodušená varianta.

Instalace python driveru: pip install cassandra-driver

V tomto cvičení se budou následující úlohy řešit s využitím DataStax driveru pro Cassandru.
Dokumentaci lze nalézt zde: https://docs.datastax.com/en/developer/python-driver/3.25/getting_started/


Optimální řešení (nepovinné) - pokud něco v db vytváříme, tak první kontrolujeme, zda to již neexistuje.


Pro uživatele PyCharmu:

Pokud chcete zvýraznění syntaxe, tak po napsání prvního dotazu se Vám u něj objeví žlutá žárovka, ta umožňuje vybrat 
jazyk pro tento projekt -> vyberte Apache Cassandra a poté Vám nabídne instalaci rozšíření pro tento typ db.
Zvýraznění občas nefunguje pro příkaz CREATE KEYSPACE.

Také je možné do PyCharmu připojit databázi -> v pravé svislé liště najděte Database a připojte si lokální Cassandru.
Řešení cvičení chceme s využitím DataStax driveru, ale s integrovaným nástrojem pro databázi si můžete pomoct sestavit
příslušně příkazy.


Pokud se Vám nedaří připojit se ke Cassandře v Dockeru, zkuste smazat kontejner a znovu spustit:

docker run --name dpb_cassandra -p 127.0.0.1:9042:9042 -p 127.0.0.1:9160:9160 -d cassandra:3.11.10

'''


def print_delimiter(n):
    print('\n', '#' * 10, 'Úloha', n, '#' * 10, '\n')


def print_result(result):
    for row in result:
        print(row)


cluster = Cluster()  # automaticky se připojí k localhostu na port 9042
session = cluster.connect()
KEYSPACE = 'dc'
"""
1. Vytvořte keyspace 'dc' a přepněte se do něj (SimpleStrategy, replication_factor 1)
"""


def task1():
    print_delimiter(1)
    session.execute("""
           CREATE KEYSPACE IF NOT EXISTS %s
           WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
           """ % KEYSPACE)
    session.set_keyspace(KEYSPACE)
    print("DONE")


"""
2. V csv souboru message_db jsou poskytnuta data pro cvičení. V prvním řádku naleznete názvy sloupců.
   Vytvořte tabulku messages - zvolte vhodné datové typy (time bude timestamp)
   Primárním klíčem bude room_id a time
   Data chceme mít seřazené podle času, abychom mohli rychle získat poslední zprávy

   Jako id v této úloze zvolíme i time - zdůvodněte, proč by se v praxi time jako id neměl používat.

   Pokud potřebujeme použít čas, tak se v praxi používá typ timeuuid nebo speciální identifikátor, tzv. Snowflake ID
   (https://en.wikipedia.org/wiki/Snowflake_ID). Není potřeba řešit v tomto cvičení.
"""


def task2():
    print_delimiter(2)
    session.set_keyspace(KEYSPACE)
    session.execute("""
        CREATE TABLE IF NOT EXISTS message_db (
            room_id text,
            speaker_id text,
            time timestamp,
            message text,
            PRIMARY KEY (room_id, time)
        )WITH CLUSTERING ORDER BY (time DESC)
        """)
    print("DONE")


"""
3. Do tabulky messages importujte message_db.csv
   COPY není možné spustit pomocí DataStax driveru ( 'copy' is a cqlsh (shell) command rather than a CQL (protocol) command)
   -> 2 možnosti:
      a) Nakopírovat csv do kontejneru a spustit COPY příkaz v cqlsh konzoli uvnitř dockeru
      b) Napsat import v Pythonu - otevření csv a INSERT dat
CSV soubor může obsahovat chybné řádky - COPY příkaz automaticky přeskočí řádky, které se nepovedlo správně parsovat
"""


def task3():
    print_delimiter(3)
    prepared = session.prepare("""
            INSERT INTO message_db (room_id, speaker_id, time, message)
            VALUES (?, ?, ?, ?)
            """)
    with open("message_db.csv", "r") as fares:
        next(fares)
        for fare in fares:
            columns = fare.split(";")
            room_id = columns[0]
            speaker_id = columns[1]
            time_ = datetime.strptime(columns[2], '%Y-%m-%d %H:%M:%S.%f')
            message = columns[3]
            session.execute(prepared, [room_id, speaker_id, time_, message])


"""
4. Kontrola importu - vypište 1 zprávu
"""


def task4():
    print_delimiter(4)
    row = session.execute('SELECT * FROM dc.message_db LIMIT 1')
    print(row.one())


"""
5. Vypište posledních 5 zpráv v místnosti 1 odeslaných uživatelem 2
    Nápověda 1: Sekundární index (viz přednáška) 
    Nápověda 2: Data jsou řazena již při vkládání
"""


def task5():
    print_delimiter(5)
    session.set_keyspace(KEYSPACE)
    session.execute("CREATE INDEX IF NOT EXISTS speaker_index ON message_db(speaker_id);")
    rows = session.execute("SELECT * FROM message_db WHERE room_id = '1' and speaker_id = '2' LIMIT 5;")
    for row in rows:
        print(row)


"""
6. Vypište počet zpráv odeslaných uživatelem 2 v místnosti 1
"""


def task6():
    print_delimiter(6)
    session.set_keyspace(KEYSPACE)
    session.execute("CREATE INDEX IF NOT EXISTS speaker_index ON message_db(speaker_id);")
    row = session.execute("SELECT count(message) FROM message_db WHERE room_id = '1' and speaker_id = '2';")
    print(row.one())


"""
7. Vypište počet zpráv v každé místnosti
"""


def task7():
    print_delimiter(7)
    session.set_keyspace(KEYSPACE)
    rows = session.execute("SELECT room_id, count(message) FROM message_db GROUP BY room_id;")
    for row in rows:
        print(row)


"""
8. Vypište id všech místností (3 hodnoty)
"""


def task8():
    print_delimiter(8)
    session.set_keyspace(KEYSPACE)
    rows = session.execute("SELECT distinct room_id FROM message_db;")
    for row in rows:
        print(row)


if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()