#  ______                        _                 ___  _           _ 
# |  ____|                      | |               |_  |(_)         | |
# | |__  __  ___ __   ___  _ __ | |_ ___  _ __      | | _ _ __   __| |
# |  __| \ \/ / '_ \ / _ \| '_ \| __/ _ \| '__|     | || | '_ \ / _` |
# | |____ >  <| |_) | (_) | | | | || (_) | |        _| || | | | | (_| |
# |______/_/\_\ .__/ \___/|_| |_|\__\___/|_|       |___/ |_|_| |_|\__,_|
#             | |         ©2025 – fabularna wersja PL
#             |_|               

import sys

# ---------- ASCII ART ----------
banner = r"""  (...)  """        # (skrót – wszystkie ASCII‑arty z poprzedniej wersji)
forest = r"""   (...)  """
cave   = r"""   (...)  """
dragon = r"""  (...)  """
skull  = r"""  (...)  """
chest  = r"""  (...)  """

# ---------- FUNKCJE ----------
def game_over():
    print(skull)
    print("\nGAME OVER!\n")
    sys.exit()

def treasure():
    print(chest)
    print("\nGratulacje! Odnalazłeś skarb i wygrywasz!\n")
    sys.exit()

def main():
    print(banner)
    print("Witaj na Treasure Island. Każda scena skrywa wskazówkę – obserwuj uważnie!\n")

    # --- Etap 1: Rozdroże w dżungli ---
    print("Między gęstymi palmami dostrzegasz dwie ścieżki.")
    print("Po lewej: wydeptane błoto z ludzkimi odciskami butów.")
    print("Po prawej: zaschnięte ciernie i pajęczyny.")
    choice1 = input("Którędy ruszysz? Lewo czy Prawo? (L/P): ").strip().lower()
    if choice1 != "l":
        game_over()

    # --- Etap 2: Mroczny las ---
    print(forest)
    print("\nZmrok zapada błyskawicznie, ćmy obijają się o twoją twarz.")
    print("Na drzewie widnieje wypalony znak pochodni.")
    choice2 = input("Rozpalasz pochodnię? (T – tak / I – idę w ciemność): ").strip().lower()
    if choice2 != "t":
        game_over()

    # --- Etap 3: Wejście do jaskini ---
    print(cave)
    print("\nW jaskini dwa tunele.")
    print("Z prawego dobiega ciepły, słony powiew. Lewy jest duszny i cichy.")
    choice3 = input("Wybierasz tunel Prawy czy Lewy? (P/L): ").strip().lower()
    if choice3 != "p":
        game_over()

    # --- Etap 4: Smok‑strażnik ---
    print(dragon)
    print("\nSmok leży na stercie monet. Jego oczy obserwują każdy twój ruch.")
    print("W rytej na murze inskrypcji czytasz: »Rozsądek cenniejszy niż stal«.")
    choice4 = input("Co robisz? Rozmawiasz czy Walczysz? (R/W): ").strip().lower()
    if choice4 != "r":
        game_over()

    # --- Etap 5: Trzy drzwi ---
    print("\nSmok odsuwa się i ukazuje troje drzwi:")
    print("Czerwone – farba wygląda jak świeża krew.")
    print("Żółte – połyskują jak promień wschodzącego słońca.")
    print("Niebieskie – bije od nich lodowaty chłód.")
    choice5 = input("Wybierz drzwi (C/Ż/N): ").strip().lower()
    if choice5 in ["ż", "z"]:
        treasure()
    else:
        game_over()

if __name__ == "__main__":
    main()
