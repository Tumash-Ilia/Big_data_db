from cassandra.cluster import Cluster
import time

'''
DPB - 12. cvičení Cassandra

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
1. Vložte libovolnou novou zprávu do místnosti 1 od uživatele 3
"""


def task_1():
    print_delimiter(1)
    session.set_keyspace(KEYSPACE)
    session.execute("INSERT INTO message_db (room_id, time, message, speaker_id) VALUES "
                    "('1', '2021-04-27 21:52:36.456', 'Test meassage', '3');")
    print("DONE")


"""
2. Smažte zprávu vloženou v bodě 7.
    Nápověda: získejte poslední záznam, čas do podmínky získáte pomocí str(result[0].time)[:-3],
        čas musí být uveden v jednoduchých uvozovkách, doporučujeme si první vypsat příkaz do konzole pro kontrolu
"""


def task_2():
    #  DELETE FROM message_db WHERE room_id = '1' and time = '2021-04-27 21:52:36.456';
    print_delimiter(2)
    session.set_keyspace(KEYSPACE)
    rows = session.execute("SELECT * FROM message_db WHERE room_id = '1' LIMIT 1;")
    time_id = str(rows.one().time)[:-3]
    session.execute("DELETE FROM message_db WHERE room_id = '1' and time = '{}';".format(time_id))
    print("DONE")

"""
3. Pro textovou analýzu chcete poskytovat anonymizovaná textová data. Vytvořte Materialized View pro tabulku messages,
který bude obsahovat pouze čas, room_id a zprávu.

Vypište jeden výsledek z vytvořeného view.
"""


def task_3():
    print_delimiter(3)
    session.execute("CREATE MATERIALIZED VIEW  IF NOT EXISTS dc.message_anon "
                    "AS SELECT room_id, time, message "
                    "FROM dc.message_db "
                    "WHERE room_id IS NOT NULL AND time IS NOT NULL "
                    "PRIMARY KEY (room_id, time);")
    rows = session.execute("SELECT * FROM dc.message_anon")
    print(rows.one())


"""
4. V aplikaci chceme navíc vytvořit feature pro tzv. mizející režim. Odeslané zprávy zmizí po 10 sekundách.

Vložte libovolnou zprávu s časovým limitem a poté ji vypište. Počkejte 10 s a zkuste ji znovu vypsat. 
"""

def task_4():
    print_delimiter(4)
    session.execute("INSERT INTO dc.message_db (room_id, time, message, speaker_id) VALUES "
                    "('1', '2021-04-27 21:52:36.456', 'Test meassage', '3')"
                    "USING TTL 10;")
    rows = session.execute("SELECT * FROM dc.message_db WHERE room_id = '1';")
    print(rows.one())
    print("Wait for 10sec")
    time.sleep(10)
    rows = session.execute("SELECT * FROM dc.message_db WHERE room_id = '1';")
    print(rows.one())
"""
5. Chceme vytvořit funkci (UDF), která při výběru dat vrátí navíc příznak, zda vybraný text obsahuje nevhodný výraz.

Vyberte jeden výraz (nemusí být nevhodný:), vytvořte a otestujte Vaši funkci.

Před začátkem řešení je potřeba jít do souboru cassandra.yaml uvnitř docker kontejneru a nastavit enable_user_defined_functions=true

docker exec -it dpb_cassandra bash
sed -i -r 's/enable_user_defined_functions: false/enable_user_defined_functions: true/' /etc/cassandra/cassandra.yaml

Poté restartovat kontejner

"""


def task_5():
    print_delimiter(5)
    session.execute("""
        CREATE FUNCTION IF NOT EXISTS dc.censor (message TEXT, word TEXT) 
        CALLED ON NULL INPUT 
        RETURNS boolean 
        LANGUAGE java AS '
         return message.contains(word);
         ';
    """)
    rows = session.execute("SELECT room_id, time, message, speaker_id, censor(message, 'the') "
                           "FROM dc.message_db "
                           "WHERE room_id = '1'"
                           "LIMIT 10;")
    for row in rows:
        print(row)

if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
