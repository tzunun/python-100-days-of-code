# Generate a name for a band

#1. Create a greetin for your program

#2. Ask the user for the city that grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure that the input cursor shows on a news line.


def generate_band_name(city: str, pet: str) -> str:
    '''This function creates the new band name.

    Parameters
    ----------
    city : str
        The city where the user grew up.
    pet : str
        The name of a pet.

    Returns:
    --------  
    str
        city and pet variables concatenated.

    '''

    return ''.join([city, " ", pet])


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
            print("Sorry, I don't understand that.\n")
            continue
        else:
            if(isinstance(answer, str) and len(answer) > 2):
                return answer
            else:
                print("Your input is not valid\n")
                continue


if __name__ == "__main__":
    print("Welcome to the Band Name Generator.\n")
    city = get_input("Please enter the name of the city were you grew up in.\n")
    pet = get_input("Please enter the name of a pet.\n")

    #print("Your band name could be {} {}".format(city, pet))
    print("Your band name could be {}\n".format(generate_band_name(city, pet)))

