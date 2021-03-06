## Cvíčení 1


Vytvořte skript task cv02.py, který bude obsahovat

* funkci **Fibonacci**, která má jeden parametr — počet prvků
  - funkce vypíše prvních n prvků Fibonacciho posloupnosti

* funkci **pyramid**, která přijímá jeden parametr — výšku pyramidy
  - funkce v textové grafice vykreslí pyramidu o zadané velikosti
* funkci **is_prime**, která přijímá jeden parametr - číslo
  - funkce vypíše, jestli je vstupní číslo prvočíslem
* funkci **pow**, která přijímá dva parametry — číslo a mocninu
  - funkce vrací výsledek mocnění
* funkci **digit_sum**, která přijímá jeden parametr — číslo
  - funkce vrací ciferný součet čísla
* funkci **is_palindrom**, která přijímá jeden parametr- řetězec
  - funkce vrací, zda-li je řetězec palindrom

[Cvíčení 1](https://github.com/Tumash-Ilia/Big_data_db/blob/main/python/cv01/task_cv02.py)

## Cvíčení 2

Vytvořte skript task cv03.py, který bude obsahovat

* funkci **save_persons**, která přijímá dva parametry
  - cestu k souboru
  - pole slovníků obsahující jednotlivé osoby (jméno, věk)
    
  a osoby ukládá do csv souboru, kde na každém řádku je jméno;věk
* funkci **load_persons**, která přijímá jeden parametr
  - cestu k souboru
    
  a vrací pole obsahující slovníky s údaji jednotlivých osob

* funkci **text_analysis**, která přijímá jeden parametr
  - cestu k textovému souboru 
    
  a vrací dvě struktury s výsledky provedené analýzy textu
  - jednotlivá písmena a počet jejich výskytů (od nejmenšího)
  - jednotlivá slova a počet jejich výskytů v textu (od největšího)
* funkci **get_words**, která přijímá tři parametry
  - počet slov N
  - minimální délku slovaM
  - strukturu z funkce text_analysis

  a vrací N slov o minimální délce M s nejvyšším výskytem (vrátit i počet)

[Cvíčení 2](https://github.com/Tumash-Ilia/Big_data_db/tree/main/python/cv02)

## Cvíčení 3

MongoDB dotazy

1. Vypsání všech restaurací
2. Vypsání všech restaurací- pouze názvy, abecedně seřazené
3. Vypsání pouze 10 záznamů z předchozího dotazu
4. Zobrazení dalších 10 záznamů
5. Vypsání restaurací ve čtvrti Bronx (čtvrť = borough)
6. Vypsání názvů restaurací, jejichž název začíná na písmeno M
7. Vypsání restaurací, které mají skóre vyšší než 80
8. Vypsání restaurací, které mají skóre mezi 80 a 90
9. Vložení nové restaurace
10. Vypsání nové restaurace
11. Aktualizace nové restaurace- změňte alespoň název
12. Smazání nové restaurace

[Cvíčení 3](https://github.com/Tumash-Ilia/Big_data_db/tree/main/MongoDB/Cv01)

## Cvíčení 4

Úloha zaměřená na komunikaci mezi Pythonem a MongoDB
* využívá stejnou databázi jako předchozí cvičení restaurants 
* úlohy jsou totožné
  - navíc je jen úloha na indexování
  - místo MongoDB shell je cílem použít PyMongo 
 
[Cvíčení 4](https://github.com/Tumash-Ilia/Big_data_db/tree/main/MongoDB/Cv02)

## Cvíčení 5

1. Zjistěte počet restaurací pro každé PSČ (zipcode)
   - seřaďte podle zipcode vzestupně
   - seřaďte podle počtu restaurací sestupně
   - výpis limitujte na 10 záznamů
  
   úlohu vyřešte pomocí agregační roury a map-reduce

2. Restaurace obsahují pole grades, kde jsou jednotlivá hodnocení.
Vypište průměrné skóre pro každou hodnotu grades.

   - vagregaci vynechte grade pro hodnotu „Not Yet Graded“ (místo A, B, atd. se
může vyskytovat)
   - výpis limitujte na 10 záznamů
    
   úlohu vyřešte pomocí agregační roury a map-reduce


[Cvíčení 5](https://github.com/Tumash-Ilia/Big_data_db/tree/main/MongoDB/Cv03)

## Cvíčení 6

ELASTICSEARCH + KIBANA

1. Vytvořte index s názvem person
2. Přidejte osobu s vaším jménem
3. Vypište vaši osobu
4. Přejmenujte vaši osobu
5. Vypište všechny dokumenty v daném indexu
6. Smažte přidanou osobu
7. Smažte vytvořený index

[Cvíčení 6](https://github.com/Tumash-Ilia/Big_data_db/blob/main/Kibana/cv01/cv07.py)

## Cvíčení 7

Vyhledávání produktů (index products)

1. vytvořte dotaz pro vyhledávání výrazu coffee“ v názvu produktu
   - kolikvýsledků se vrátí?

2. upravte dotaz tak, aby se zobrazily stejné výsledky, pokud uživatel udělá
jeden překlep
  - např. stejné výsledky pro,cofee' nebo,coffe“
  - cosestane po povolení více než jednoho překlepu?

3. vytvořte dotaz, který vyhledá produkty s tagem Coffee“
   - lišíse počet výsledků?
   - pokudano,který název nenalezl první dotaz a proč?

4. najděte produkty s tagem,Coffee“ s 10 nebo méně kusy na skladě (in stock)

5. najděte produkty, které v názvu mají ,coffee, ale neobsahují „cup“

Vyhledávání receptů (index recipes)

6. vytvořte dotaz, který bude vracet recepty, v nichž se nachází libovolný výraz
   - hledaný výraz může být v nadpisu, popisu nebo ingrediencích receptu

Vyhledávání produktů (index products)

7. vytvořte dotaz, který bude fungovat jako našeptávač při vyhledávání
   - začne vracet nejvíce relevantní výsledky během psaní
   - např. uživatel napíše pouze znak,c' a už jsou mu vraceny první výsledky
   - zadaný řetězec se může nacházet kdekoliv v názvu
   - doporučujte pouze 5 relevantních produktů
   - vyzkoušejte si postupně vyhledávat,c,co; ...,.coffee“


[Cvíčení 7](https://github.com/Tumash-Ilia/Big_data_db/blob/main/Elasticsearch_Kibana/cv02/elastic_first.txt)

## Cvíčení 8

Mapování
1. vytvořte mapování pro definici struktury indexu pro objednávky
   - index nazvěte orders-new
   - index bude umožňovat objednávky produktů z indexu products
(viz minulé cvičení)
   - vymyslete vhodnou strukturu objednávky a vhodné datové typy
   - není potřeba vymýšlet až hodnot, např. pro zákazníka stačí jméno

2. vložte záznam do vytvořeného indexu
   - objednávka musí obsahovat kávu a další dva libovolné produkty
    
Agregace (nad indexem products)

1. zjistěte maximální, minimální a průměrnou cenu produktů
   - bez použití stats

2. zjistěte maximální, minimální a průměrný počet prodaných
produktů
   - použitím stats
   - pomocí dalšího dotazu zjistěte, který produkt se prodává nejvíce

3. pro každý tag zjistěte, v kolika dokumentech je obsažen

4. zjistěte cenové statistiky pro jednotlivé tagy (vnořená agregace)
   - do 3.úlohy přidat stats

5. získejte statistiky pouze pro produkty s tagem Coffee“ a ,Cake' (filter)

Analyzéry

1. vyzkoušejte si 3 analyzéry pomocí POST analyze


[Cvíčení 8](https://github.com/Tumash-Ilia/Big_data_db/blob/main/Elasticsearch_Kibana/cv03/elastic_2.txt)


## Cvíčení 9

Cassandra 

1. vytvořte keyspace cass01
   - SimpleStrategy, replication factor 1

2. ověřte vytvoření keyspace a následně se do ní přepněte
3. vytvořte tabulku activity se dvěma sloupci id a datetime
   - primární klíč je id a datetime, řazení podle datetime sestupně
4. do tabulky přidejte sloupec event (text) a ověřte, že byl přidán
5. vložte jeden libovolný záznam
6. vložte libovolný druhý záznam s aktuální timestamp hodnotou
   - ne vloženou ručně
7. vypište vložené záznamy
8. smažte vytvořené záznamy, tabulku a následně i keyspace


[Cvíčení 9](https://github.com/Tumash-Ilia/Big_data_db/blob/main/Cassandra/cv01/cassandra.txt)


## Cvíčení 10

1. vytvořte keyspace dc a přepněte se do něj
   - SimpleStrategy, replication factor 1

2. vytvořte tabulku message db pro data z messages db.csv
   - vhodně zvolte datové typy, jako primární klíč nastavte room id a time

3. do tabulky message db importujte data z messages db.csv
4. vypište jednu zprávu

5. vypište 5 posledních zpráv v místnosti 1 odeslaných uživatelem 2
6. vypište počet zpráv odeslaných uživatelem 2 v místnosti 1
7. vypište počet zpráv v každé místnosti

8. vypište id všech místností (3 hodnoty)


[Cvíčení 10](https://github.com/Tumash-Ilia/Big_data_db/tree/main/Cassandra/cv02)


## Cvíčení 11

1. vložte libovolnou novou zprávu do místnosti 1 od uživatele 3
2. smažte vámi vloženou zprávu

3. vytvořte materialized view pro tabulku messages, který bude
obsahovat pouze čas, room id a zprávu
  - vypište jeden výsledek z vytvořeného view

4. vložte libovolnou zprávu s časovým limitem 10 s, vypište ji
   - po 10s ji zkuste vypsat znovu

5. vytvořte vlastní funkci, která při výběru dat vrátí navíc příznak, zda
vybraný text obsahuje nevhodný výraz
   - vyberte jeden výraz (nemusí být nevhodný) a otestujte

[Cvíčení 11](https://github.com/Tumash-Ilia/Big_data_db/tree/main/Cassandra/cv03)


## Cvíčení 12

1. vypište 10 libovolných uzlů
2. vypište 10 libovolných filmů
3. vypište herce, kteří hráli ve filmu TheMatrix, seřaďte je podle jména
4. vypište filmy, ve kterých hrál Keanu Reeves
5. vypište počet filmů, ve kterých hrál Keanu Reeves
6. vypište filmy, ve kterých hrál Keanu Reeves a Carrie-Anne Moss
7. vypište průměrný výdělek herců
8. přidejte nový film „John Wick“, ve kterém bude hrát Keanu Reeves
9. upravte herce Keanu Reeves, přidejte libovolnou vlastnost

[Cvíčení 12](https://github.com/Tumash-Ilia/Big_data_db/blob/main/Neo4j/neo.txt)



