from random import randint

def display_hand(gesture: str) -> None:
    match gesture:
        case "Rock":
            print('''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''')
        case "Paper":
            print('''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            ''')
        case "Scissors":
            print('''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___) 
            ''')
            pass

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
                return answer
            else:
                print("Invalid choice.\n Good bye!")
                quit()

def player_chooses() -> int:
    return int(get_input("What do you choose?\nEnter 0 for Rock, 1 for Paper or 2 for Scissors. "))

def computer_chooses() -> int:
    return randint(0, 2)

def check_game_status(player:int, computer:int) -> None:
    hand_gestures = ["Rock", "Paper", "Scissors"]
    print("Player chooses: {}".format(hand_gestures[player]))
    display_hand(hand_gestures[player])
    print("Computer chooses: {}".format(hand_gestures[computer]))
    display_hand(hand_gestures[computer])

    if player == computer:
        print("It is a tie.") 
    elif (player + 1) % 3 == computer:
        print("Computer wins.")
    else:
        print("Player wins.")

if __name__ == "__main__":
    player = player_chooses()
    while player <0 or player >2:
        print("Invalid input '{}'".format(player))
        player = player_chooses()
    computer = computer_chooses()
    check_game_status(player, computer)
