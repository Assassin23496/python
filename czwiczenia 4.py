import cmath
from math import factorial

n = 5
s = 1
for i in range(1,n + 1):
    s*=i
print(s)

a = 1
c = 0
while (a < 3):
    for b in range(1,3):
        c += a + b + 1
        c += 8
    a += 1
print(c)

#zad2a
def dziel(a, b):
    if b != 0:
        wynik = a / b
        print(f"Wynik dzielenia {a} przez {b} to: {wynik}")
    else:
        print("Dzielenie przez zero nie jest możliwe.")
dziel(5.0, 2)
dziel(3, 0)




#zad2b
def konvertT(a,znak):
    if znak!='F' and znak!='C':
        return 0
    elif(znak=='F'):
        return  a*1.8+32
    else:
        return (a-32)/1.8
print(konvertT(3.2,'C'))

#czwiczenia 3
def liczba_cyfr(liczba):
    # Jeśli liczba jest ujemna, zamieniamy ją na dodatnią
    if liczba < 0:
        liczba = -liczba

    # Specjalny przypadek dla liczby 0, która ma 1 cyfrę
    if liczba == 0:
        return 1

    licznik = 0

    # Liczymy cyfry poprzez dzielenie liczby przez 10
    while liczba > 0:
        liczba //= 10
        licznik += 1

    return licznik


# Główna funkcja wczytująca liczbę i wypisująca wynik
if __name__ == "__main__":
    liczba = int(input("Podaj liczbę: "))
    wynik = liczba_cyfr(liczba)
    print(f"Liczba cyfr: {wynik}")

def czy_pirwsza(a):
    if liczba<2:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            return 0
    return 1
if __name__ == '__main__':
    liczba = 5
    if czy_pirwsza(liczba):
        print(liczba,"Jest pirwsza")
    else:
        print(liczba," Nie jest liczba pierwsza")
#zad 3

def rozwiaz_kwadratowe(a, b, c):
    # Przypadek, gdy a = 0, równanie przekształca się w liniowe
    if a == 0:
        if b == 0:
            if c == 0:
                return "Nieskończenie wiele rozwiązań"  # 0 = 0
            else:
                return "Brak rozwiązań"  # c = 0 (sprzeczność)
        else:
            # Równanie liniowe: bx + c = 0
            x = -c / b
            return f"Równanie liniowe, rozwiązanie: x = {x}"

    # Obliczamy deltę (Δ = b^2 - 4ac)
    delta = b ** 2 - 4 * a * c

    # Sprawdzamy czy delta jest ujemna, zerowa, czy dodatnia
    if delta > 0:
        # Dwa różne rozwiązania rzeczywiste
        x1 = (-b + cmath.sqrt(delta).real) / (2 * a)
        x2 = (-b - cmath.sqrt(delta).real) / (2 * a)
        return f"Dwa rozwiązania rzeczywiste: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        # Jedno rozwiązanie rzeczywiste
        x = -b / (2 * a)
        return f"Jedno podwójne rozwiązanie rzeczywiste: x = {x}"
    else:
        # Dwa rozwiązania zespolone
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return (f"Dwa rozwiązania zespolone: \n"
                f"x1 = {x1.real} + {x1.imag}i \n"
                f"x2 = {x2.real} + {x2.imag}i")


if __name__ == "__main__":

 a = float(input("Podaj współczynnik a: "))
 b = float(input("Podaj współczynnik b: "))
 c = float(input("Podaj współczynnik c: "))

    # Wywołujemy funkcję rozwiązującą równanie kwadratowe
 wynik = rozwiaz_kwadratowe(a, b, c)

    # Wyświetlamy wynik
 print(wynik)

def sgn(x):
    if x<0:
        return -1
    elif x>0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    x=float(input("Wpisz dowolna liczbe:"))
    wynik1=sgn(x)
    print(wynik1)



def oblicz(n):
    e1 =(1+1/n)**n
    e2=0
    for k in range(0,n):
        e2 += 1/factorial(k)
    return e1,e2
n=int(input("podaj liczbe:"))
print(oblicz(n))