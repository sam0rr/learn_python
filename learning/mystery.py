import random

MIN = 1
MAX = 100

def donner_indice(distance):
    if distance >= 50:
        return "\nTu es très loin !"
    elif distance >= 20:
        return "\nTu es loin !"
    elif distance >= 10:
        return "\nTu te rapproches !"
    elif distance >= 5:
        return "\nTu es proche !"
    else:
        return "\nTu es brûlant !!!"

def menu():
    while True:
        print("\n--Random Game--")

        choice = ""
        while choice not in ["1", "0"]:
            choice = input("\nChoisir (1 jouer, 0 quitter): ")

            if choice not in ["1", "0"]:
                print("\nChoisir invalide.")

        if choice == "1":
            game()

        if choice == "0":
            return

def ask_number():
    valid_input = False

    while not valid_input:
        try:
            guess = int(input("Guess : "))
            valid_input = True
        except ValueError:
            print("\nLa valeur n'est pas valide. Veuillez entrer un nombre entier.")

    return guess

def game():
    number = random.randint(MIN, MAX)
    print("\n--Veuillez deviner le nombre random--\n")
    print(f"Indice: il s'agit d'un nombre entre {MIN} et {MAX}\n ")

    guess = None
    attempts = 0

    while guess != number:

        guess = ask_number()

        attempts += 1

        distance = abs(number - guess)

        print(donner_indice(distance))

    print(f"\nBravo ! Vous avez trouvé le nombre {number} en {attempts} tentatives.")

if __name__ == '__main__':
    menu()
