import string
from random import shuffle, choice

def generate_password(length, use_numbers, use_capital, use_special_chars):
    chars = string.ascii_letters.lower()

    if use_numbers:
        chars += string.digits
    if use_capital:
        chars += string.ascii_uppercase
    if use_special_chars:
        chars += string.punctuation

    password = []

    if use_special_chars:
        password.append(choice(string.punctuation))
    if use_numbers:
        password.append(choice(string.digits))
    if use_capital:
        password.append(choice(string.ascii_uppercase))

    password += [choice(chars) for _ in
                 range(length - len(password))]

    shuffle(password)

    return "".join(password)

def password_rules ():
    use_numbers = input("Voulez-vous utiliser des chiffre (O/N)").strip().lower() == "o"
    use_capital = input("Voulez-vous utiliser des majuscules (O/N)").strip().lower() == "o"
    use_special_chars = input("Voulez-vous inclure des charactère spéciaux (O/N)").strip().lower() == "o"

    return use_numbers, use_capital, use_special_chars

def length_tester ():
    while True:
        try:
            length = int(input("Entrer la longueur du mot de passe : "))
            if length < 50:
                return length
            else:
                print("password trop long.")
        except ValueError:
            print("Veuillez saisir un nombre valide.")

def main():
    print("\n---Générateur de mot de passe alphanumérique---")

    length = length_tester()

    use_numbers, use_capital, use_special_chars = password_rules()

    password = generate_password(length, use_numbers, use_capital, use_special_chars)

    print(f"Voici votre mot de passe : {password}")

if __name__ == '__main__':
    main()
