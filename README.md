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



[Cvíčení 8](https://github.com/Tumash-Ilia/Big_data_db/blob/main/python/cv01/task_cv02.py)


## Cvíčení 1

[Cvíčení 1](https://github.com/Tumash-Ilia/Big_data_db/blob/main/python/cv01/task_cv02.py)


## Cvíčení 1

[Cvíčení 1](https://github.com/Tumash-Ilia/Big_data_db/blob/main/python/cv01/task_cv02.py)


## Cvíčení 1

[Cvíčení 1](https://github.com/Tumash-Ilia/Big_data_db/blob/main/python/cv01/task_cv02.py)


