import math

max_number = 200

def up_to():
    numbers = range(2, max_number)
    primes = []

    for number in numbers:
        is_prime = True
        for divisor in range(2, int(math.sqrt(number)) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)

    print("\nTous les nombres premiers :")
    for prime in primes:
        print(prime)

def one_number():
    number = ask_number()
    for divisor in range(2, int(math.sqrt(number)) + 1):
            if number % divisor == 0:
                return print(f"\nLe nombre {number} est premier")
            else:
                return print(f"\nLe nombre {number} n'est pas premier")

def ask_number():
    valid = False

    while not valid:
        try:
            number = int(input("\nRentrer votre nombre premier: "))
            valid = True
        except ValueError:
            print("\nEntrée invalide ! Veuillez entrer des valeurs numériques.")

    return number

def main():
    while True:
        print("\nPrime tester :\n")
        choice = 0

        while choice not in [1, 2, 3]:
            print(f"1-   Tester tous les nombres premiers ({max_number})")
            print("2-   Tester un nombre")
            print("3-   Quitter")

            try:
                choice = int(input())
            except ValueError:
                print("\nEntrée invalide ! Veuillez entrer un nombre valide.")

            if choice not in [1, 2, 3]:
                print("\nChoix invalide ! Veuillez entrer 1, 2 ou 3.")

        if choice == 3:
            print("\n\nE N D.")
            return

        if choice == 1:
            up_to()

        if choice == 2:
            one_number()

if __name__ == '__main__':
    main()
