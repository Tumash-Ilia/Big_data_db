"""
Cv_03
"""
import csv


def save_persons(path, person_arr):
    with open(path, "w", newline="") as file_csv:
        writer = csv.DictWriter(file_csv, delimiter=';', fieldnames=person_arr[0].keys())
        writer.writerows(person_arr)


def load_persons(path):
    persons_list = []
    try:
        with open(path, "r", newline="") as file_csv:
            reader = csv.DictReader(file_csv, delimiter=';', fieldnames=["name", "age"])
            for row in reader:
                persons_list.append(row)
    except FileNotFoundError:
        print("File not found, check path:'{}'".format(path))
    return persons_list


def text_analysis(path):
    try:
        with open(path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found, check path:'{}'".format(path))
    content = content.lower()  # Registr pismen, hledame pismena bez ohledu na registr
    symbols = {sym: content.count(sym) for sym in set(content)}
    for sym in set(content):  # Odstranim ze slovniku interpunkcni znamenka a mezery
        if not sym.isalpha():
            symbols.pop(sym, None)
    list_s = list(symbols.items()) # Protoze slovnik je neusporadana structura dat, udelam ze slovniku list tuplu
    list_s.sort(key=lambda i: i[1]) # Usporadam list podle poctu vyskytu pismen
    content = content.replace("\n", " ") # Najdu slova v textu
    content = content.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    content = content.lower()
    words = content.split()
    words_dict = dict()   # Vytvarim slovnik slov
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    list_w = list(words_dict.items())  # Usporadam list podle poctu vyskytu slov
    list_w.sort(key=lambda i: i[1], reverse=True)
    return list_s, list_w


def get_words(count_n, min_len, struct):
    words = []
    for i in struct:
        if len(i[0]) >= min_len:
            words.append(i)
            if len(words) == count_n:
                return words
    return words


if __name__ == '__main__':
    """
    persons = [
        {"name": "Person1", "age": 17},
        {"name": "Person2", "age": 32},
        {"name": "Person3", "age": 24}
    ]
    path = "persons.csv"
    save_persons(path, persons)
    p = load_persons(path)
    print("\nLoad persons")
    for i in p:
        print(i)
    list_s, list_w = text_analysis("text.txt")
    print("\nPismena v textu:")
    for i in list_s:
        print(i[0], '-', i[1])
    print("\nSlova v textu:")
    for i in list_w:
        print(i[0], '-', i[1])
    print('\nGet words:')
    words = get_words(6, 3, list_w)
    for i in words:
        print(i[0], '-', i[1])
    """