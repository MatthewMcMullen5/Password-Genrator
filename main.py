import random


class bcolors:
    true = "\033[93m"
    RESET = '\033[0m'


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


def _input(message, input_type=str):
    while True:
        try:
            return input_type(input(message))
        except:
            pass


r1 = Guide()
yes_or_no = ["yes", "no"]


def reset():
    r = input("Do you want to start over? Yes/No ").lower()
    if r == "yes":
        initiate()
    if r == "no":
        quit()


def initiate():
    r1.characters = ""
    r1.has_symbols = False
    r1.has_numbers = False
    r1.has_lower = False
    r1.has_upper = False
    r1.has_similar = False
    r1.has_ambiguous = False

    choices = ["How many characters? (press Q at any time to quit/restart) ",
               "Do you want symbols (e.g. @#$%)? Yes/No ",
               "Do you want numbers (e.g. 123456)? Yes/No ",
               "Do you want lower case letters (e.g. abcdefgh)? Yes/No ",
               "Do you want upper case letters (e.g. ABCDEFGH)? Yes/No ",
               "Do you want similar characters (e.g. i, l, 1, L, o, 0, O)? Yes/No ",
               "Do you want ambiguous characters (e.g. { } [ ] ( ) ' ` ~ , ; : . < >)? Yes/No ",
               "Are the parameters above correct? Yes/No "]

    x = 0

#   loop through choices and assign values.
    for y in choices:
        r1.display()
        if x == 0:
            answer = _input(choices[x], int)
            r1.characters = answer

        else:
            answer = input(choices[x]).lower()
            if answer == "yes":
                if x == 1:
                    r1.has_symbols = True
                if x == 2:
                    r1.has_numbers = True
                if x == 3:
                    r1.has_lower = True
                if x == 4:
                    r1.has_upper = True
                if x == 5:
                    r1.has_similar = True
                if x == 6:
                    r1.has_ambiguous = True
                if x == 7:
                    continue
            if answer == "no":
                if x == 1:
                    r1.has_symbols = False
                if x == 2:
                    r1.has_numbers = False
                if x == 3:
                    r1.has_lower = False
                if x == 4:
                    r1.has_upper = False
                if x == 5:
                    r1.has_similar = False
                if x == 6:
                    r1.has_ambiguous = False
                if x == 7:
                    reset()
            if answer == "q":
                reset()
                break
            if answer not in yes_or_no:
                continue

        x += 1


initiate()

# Use information to generate random password
password_symbols = ["!", "@", "#", "$", "%", "^",
                    "&", "*", "_", "-", "=", "+", "?"]
password_numbers = ["1", "2", "3", "4", "5",
                    "6", "7", "8", "9", "0"]
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
password_similar = ["i", "I", "l", "1",
                    "L", "o", "O", "0"]
password_ambiguous = ["{", "}", "[", "]",
                      "(", ")", "/", "'",
                      "`", "~", ";", ":",
                      ".", "<", ">"]
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
    password_key.append(r1.has_similar)
if r1.has_ambiguous:
    password_key += password_ambiguous


def generate_password():
    password = ""
    for x in range(0, r1.characters):
        password += random.choice(password_key)
    print(password)


while True:
    generate_password()
    repeat = input("Would you like to generate another with these same parameters? ").lower()

    if repeat not in yes_or_no:
        continue

    if repeat == "yes":
        for i in range(int(_input("How many passwords do you want to generate? ", int))):
            generate_password()
        continue

    if repeat == "no":
        reset()

    else:
        continue
