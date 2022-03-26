import math


def fibonacci(pocet):
    a = 0
    b = 1
    for __ in range(pocet + 1):
        print(a, end=" ")
        a, b = b, a + b
    print()


def pyramid(vyska):
    for i in range(vyska):
        print(' ' * (vyska - i - 1), end="")
        print("*" * (2 * i + 1))


def is_prime(cislo):
    for i in range(2, int(round(math.sqrt(cislo)))+1):
        if cislo % i == 0:
            print(str(cislo) + " neni prvocislo")
            return
    print(str(cislo) + " je prvocislo")

def pow(a, b):
    return a ** b


def digit_sum(cislo):
    sum = 0

    while cislo > 0:
        digit = cislo % 10
        sum = sum + digit
        cislo = cislo // 10
    return sum

def is_palindrom(a):
    a = a.lower()
    a = a.replace(' ', '')
    return a == a[::-1]


if __name__ == '__main__':
    print("Fibonacci 6 8 10")
    fibonacci(6)
    fibonacci(8)
    fibonacci(10)

    print("Pyramid 3 5")
    pyramid(3)
    pyramid(5)
    print("Is prime 2 3 6 11")

    is_prime(2)
    is_prime(3)
    is_prime(6)
    is_prime(11)

    print("Pow 2^3 2^10")
    print(pow(2,3))
    print(pow(2,10))

    print("Digit_sum 23 235 500")
    print(digit_sum(23))
    print(digit_sum(235))
    print(digit_sum(500))

    print("Palindrom 'kajak'  'madam' 'pyhon' 'Kuna nese nanuk'")
    print(is_palindrom("kajak"))
    print(is_palindrom("madam"))
    print(is_palindrom("python"))
    print(is_palindrom("Kuna nese nanuk"))

