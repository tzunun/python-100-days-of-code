from random import randint
from random import shuffle
import string

def generate_password(number_of_letters: int, number_of_symbols: int, number_of_numbers: int) -> str:
    '''This function generates a password based on the constraints specified by the user.

    Parameters
    __________
    number_of_letters
        An int which is the number of letters in the generated password.

    number_of_symbols
        An int which is the number of symbols in the generated password.

    number_of_numbers
        An int which is the amount of numbers in the generated password.

    Returns
    -------
    str
        The user's new generated password.  The total length is the sum of all of the arguments given to the function.
    
    '''

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    numbers_length = len(numbers)-1
    symbols_length = len(symbols)-1
    letters_length = len(letters)-1

    password = []
    for i in range(1, number_of_numbers+1):
        password.append(numbers[randint(0,numbers_length)])
    for i in range(1, number_of_symbols+1):
        password.append(symbols[randint(0,symbols_length)])
    for i in range(1, number_of_letters+1):
        password.append(letters[randint(0,letters_length)])

    shuffle(password)
    return ''.join(password)

def get_input(desired_input: str) -> str:
    '''This functions obtains the desired string input and performs data
    validation.

    Parameters
    ----------
    desired_input
        A string variable that will become part of the input requested from
        the user.

    Returns
    -------
    str
        The user's answer to the desired input.

    '''

    answer = ''

    while True:
        try:
            answer = input(desired_input)
        except ValueError:
            print("Sorry, I don't understand that.")
            continue
        else:
            if answer.isdigit():
                return int(answer)
            else:
                print("Invalid choice.\n Good bye!")
                quit()

if __name__ == "__main__":
    print("Welcome to PyPassword Generator!")
    letters = get_input("How many letters would you like in you password? ")
    symbols = get_input("How many symbols would you like in you password? ")
    numbers = get_input("How many numbers would you like in you password? ")
    password = generate_password(letters,symbols,numbers)
    print("Password: {}".format(password))