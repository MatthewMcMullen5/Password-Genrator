import random


class bcolors:
    true = "\033[93m"
    RESET = '\033[0m'


def _input(message, input_type=str):
    while True:
        try:
            return input_type(input(message))
        except:
            pass


class Guide():
    def display(self):
        print(bcolors.true +
              "\n",
              f"Characters:{r1.characters}, "
              f"Symbols:{r1.has_symbols}, "
              f"Numbers:{r1.has_numbers}, "
              f"Lower:{r1.has_lower}, "
              f"Upper:{r1.has_upper}, "
              f"Similar:{r1.has_similar}, "
              f"Ambiguous:{r1.has_ambiguous}.",
              "\n" + bcolors.RESET)


r1 = Guide()
r1.characters = ""
r1.has_symbols = False
r1.has_numbers = False
r1.has_lower = False
r1.has_upper = False
r1.has_similar = False
r1.has_ambiguous = False

yes_or_no = ["yes", "no"]

# input desired generation.
while True:
    r1.display()
    r1.characters = _input("How many characters? ", int)
    break

while True:
    r1.display()
    r1.has_symbols = input("Do you want symbols (e.g. @#$%)? Yes/No ").lower()

    if r1.has_symbols not in yes_or_no:
        continue

    elif r1.has_symbols == "yes":
        r1.has_symbols = True

    elif r1.has_symbols == "no":
        r1.has_symbols = False

    break

while True:
    r1.display()
    r1.has_numbers = input("Do you want numbers (e.g. 123456)? Yes/No ").lower()

    if r1.has_numbers not in yes_or_no:
        continue

    elif r1.has_numbers == "yes":
        r1.has_numbers = True

    elif r1.has_numbers == "no":
        r1.has_numbers = False

    break

while True:
    r1.display()
    r1.has_lower = input("Do you want lower case letters (e.g. abcdefgh)? Yes/No ").lower()

    if r1.has_lower not in yes_or_no:
        continue

    elif r1.has_lower == "yes":
        r1.has_lower = True

    elif r1.has_lower == "no":
        r1.has_lower = False

    break

while True:
    r1.display()
    r1.has_upper = input("Do you want upper case letters (e.g. ABCDEFGH)? Yes/No ").lower()

    if r1.has_upper not in yes_or_no:
        continue

    elif r1.has_upper == "yes":
        r1.has_upper = True

    elif r1.has_upper == "no":
        r1.has_upper = False

    break

while True:
    r1.display()
    r1.has_similar = input("Do you want similar characters (e.g. i, l, 1, L, o, 0, O)? Yes/No ").lower()

    if r1.has_similar not in yes_or_no:
        continue

    elif r1.has_similar == "yes":
        r1.has_similar = True

    elif r1.has_similar == "no":
        r1.has_similar = False

    break

while True:
    r1.display()
    r1.has_ambiguous = input("Do you want ambiguous characters (e.g. { } [ ] ( ) ' ` ~ , ; : . < >)? Yes/No ").lower()

    if r1.has_ambiguous not in yes_or_no:
        continue

    elif r1.has_ambiguous == "yes":
        r1.has_ambiguous = True

    elif r1.has_ambiguous == "no":
        r1.has_ambiguous = False

    break

while True:
    r1.display()
    is_correct = input("Are the parameters above correct? Yes/No ").lower()

    if is_correct not in yes_or_no:
        continue

    elif is_correct == "no":
        exit()

    elif is_correct == "yes":
        break

# Use information to generate random password
password_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "=", "+", "?"]
password_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
password_lower = ["a", "b", "c", "d", "e", "f",
                  "g", "h", "i", "j", "k", "l",
                  "m", "n", "o", "p", "q", "r",
                  "s", "t", "u", "v", "w", "x",
                  "y", "z"]
password_upper = ["A", "B", "C", "D", "E", "F",
                  "G", "H", "I", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R",
                  "S", "T", "U", "V", "W", "X",
                  "Y", "Z"]
password_similar = ["i", "I", "l", "1", "L", "o", "O", "0"]
password_ambiguous = ["{", "}", "[", "]", "(", ")", "/",
                      "'", "`", "~", ";", ":", ".", "<", ">"]
password_key = []

if r1.has_symbols:
    password_key += password_symbols
if r1.has_numbers:
    password_key += password_numbers
if r1.has_lower:
    password_key += password_lower
if r1.has_upper:
    password_key += password_upper
if r1.has_similar is False:
    # for
    password_key.append(r1.has_similar)
if r1.has_ambiguous:
    password_key += password_ambiguous


def generate_password():
    password = ""
    for x in range(0, r1.characters):
        password += random.choice(password_key)
    print(password, "\n")


generate_password()

while True:
    repeat = input("Would you like to generate another with these same parameters? ").lower()
    if repeat not in yes_or_no:
        continue
    if repeat == "yes":
        generate_password()
        continue
    if repeat == "no":
        break
