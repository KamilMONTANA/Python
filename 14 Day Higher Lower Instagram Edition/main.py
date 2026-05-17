from art import logo, vs
from data import data
import random

"""
Gra Higher Lower Instagram Edition - gra polega na odgadnięciu osoby, która ma więcej followersów na Instagramie.
1. Wylosuj dwie osoby z bazy danych.
2. Porównaj ich liczbę followersów.
3. Zadaj użytkownikowi pytanie, który z nich ma więcej followersów.
4. Sprawdź, czy jego odpowiedź jest poprawna.
5. Jeśli jest poprawna, zwiększ punktację, wypisz ją i kontynuuj grę.
6. Jeśli jest niepoprawna wypisz punktację i zakończ grę.
7. Po każdej rundzie wygranej czy przegranej wyświetla liczbę followersów każdej z opcji. 
"""

game = True
score = 0

while game:
    print(logo)

    person1 = random.choice(data)
    person2 = random.choice(data)

    if person1["follower_count"] > person2["follower_count"]:
        higher = person1
        lower = person2
    else:
        higher = person2
        lower = person1

    print(
        f"\nWybierz: Opcja A: {higher['name']}, {higher['description']}, {higher['country']}"
    )
    print(f"{vs}")
    print(f"Opcja B: {lower['name']}, {lower['description']}, {lower['country']}")
    guess = input("Kto ma więcej followersów? Wpisz 'A' lub 'B': ")

    if guess.upper() not in ["A", "B"]:
        print("Nie ma takiej odpowiedzi!")
        game = False

    if (guess.upper() == "A" and person1 == higher) or (
        guess.upper() == "B" and person2 == higher
    ):
        score += 1
        print("Poprawna odpowiedź!")
        print(f"Twoja aktualna punktacja: {score}")
    else:
        print("Niestety, to nie jest poprawna odpowiedź.")
        print(f"Twoja końcowa punktacja: {score}")
        game = False
