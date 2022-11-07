# Calculate the tip of a bill
# First obtain the total bill amount.
# Then obtain the tip amount that the user would like to give.
# Ask how many people are goint to split the bill.
# Display the amount each pearson should pay, by first calculating the tip percentage and then split it into 
#  however many people.

def is_float(answer: str) -> bool:
    '''This function check for a float

    Parameters
    ----------
    answer : str
        the input from the user.

    Returns 
    _______
    bool
        True if the input is a float value, False otherwise

    '''
    try:
        float(answer)
        return True
    except ValueError:
        return False


def calculate_individual_amount(bill_total: float, tip_percentage: int, number_of_individuals: int) -> float:
    '''This function calculates how much is the bill per individual.

    Parameters
    ----------
    bill_total : float
        The total bill amount.
    tip_percentage : int
        The tip percentage that has to be added to the bill.
    number_of_individuals : int
        Number of individuals that are splitting the bill

    Returns
    --------  
    float
        The amount that each individual should pay.

    '''

    return round(((bill_total * tip_percentage/100) + bill_total)/number_of_individuals, 2)


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
            if answer.isnumeric() or is_float(answer) :
                return answer
            else:
                print("Your input is not valid.")
                continue


if __name__ == "__main__":
    print("Welcome to the tip calculator.")
    total_bill = get_input("What was the total bill? $")
    tip_percentage = get_input("What percentage tip would you like to give? 10, 12 or 15? ")
    
    while not (tip_percentage == "10" or tip_percentage == "12" or tip_percentage == "15"):
        tip_percentage = get_input("What percentage tip would you like to give? 10, 12 or 15? ")

    number_of_individuals = get_input("How many people to split the bill? ")
    individual_amount = calculate_individual_amount(float(total_bill), int(tip_percentage), int(number_of_individuals) )

    print("Each person should pay ${}\n".format(individual_amount))