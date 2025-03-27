from collections import Counter
from pynput import keyboard
import os

def count(string):
    return dict(Counter(string))

should_quit = False

def close_game(key):
    if key == keyboard.Key.esc:
        print("\n\nFermeture immédiate du jeu...")
        os._exit(0)

def validate_query():
    while True:
        name = input("Entrer le mot à deviner : ").strip().lower()
        if name.isalpha():
            return name
        else:
            print("\nLe mot doit contenir uniquement des lettres.")

def attempts_loop(name, letters_counter, guessed_letters, attempts):
    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in name])
        print(f"\nMot à deviner : {display_word}")
        print(f"\nTentatives restantes : {attempts}")

        guess = input("\nDevinez une lettre : ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("\nVeuillez entrer une seule lettre valide.")
            continue

        if guess in guessed_letters:
            print("\nVous avez déjà deviné cette lettre.")
            continue

        guessed_letters.add(guess)

        if guess in letters_counter:
            print("\nBien joué !")
            if all(letter in guessed_letters for letter in name):
                print(f"\nFélicitations, vous avez trouvé le mot : '{name}' !")
                break
        else:
            attempts -= 1
            print("Lettre incorrecte.")

    if attempts == 0:
        print(f"Perdu ! Le mot était '{name}'.")

def game_loop(name):
    letters_counter = count(name)
    guessed_letters = set()
    attempts = len(name) + 3

    print("\nDébut du jeu !")

    attempts_loop(name, letters_counter, guessed_letters, attempts)

def main():
    while not should_quit:

        print(should_quit)
        print("\n[-****-] Jeu de Hangman [-****-]")
        print("\nAppuyez sur ESC à tout moment pour quitter.\n")

        listener = keyboard.Listener(on_release=close_game)
        listener.start()

        name = validate_query()
        game_loop(name)

        listener.stop()

if __name__ == '__main__':
    main()
