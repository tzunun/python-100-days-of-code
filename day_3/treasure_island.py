
def display_ascii_art() -> None:
    print('''
                               o                    
                           _---|         _ _ _ _ _ 
                        o   ---|     o   ]-I-I-I-[ 
       _ _ _ _ _ _  _---|      | _---|    \ ` ' / 
       ]-I-I-I-I-[   ---|      |  ---|    |.   | 
        \ `   '_/       |     / \    |    | /^\| 
         [*]  __|       ^    / ^ \   ^    | |*|| 
         |__   ,|      / \  /    `\ / \   | ===| 
      ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
      I_I__I_I__I_I  (====(_________)___|_|____|____
      \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
       |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
       |.   | |' |___|_____I___|___I___|---------| 
      / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
     <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
     ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
     ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
     <===>     ' ||||| |   |   | ||||.||  []   <===>
      \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
       |      . _||||| |   |   | ||||.|| |     | |
    ../|' v . | .|||||/____|____\|||| /|. . | . ./
    .|//\............/...........\........../../\\\
    \n''')

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
            return answer.lower()

def player_chooses(options: str, choice: str) -> str:
    match options:
        case "direction":
            if choice == "left":
                return "ok"
            else:
                return "You fall into a hole.  Game over."
        case "action":
            if choice == "wait":
                return "ok"
            else:
                return "Attack by trout.  Game over."
        case "choose":
            if choice == "yellow":
                return "You win."
            if choice == "blue":
                return "Eaten by beasts.  Game over."
            if choice == "red":
                return "Burned by fire.  Game over."
            else:
                return "Abducted by the dark side.  Game over."

def check_game_status(status: str) -> None:
    print(status)
    if not status == "ok":
        quit()


if __name__ == "__main__":
    display_ascii_art()
    print("Welcome to Treasure Castle.")
    print("Your mission is to find the treasure.")
    print("You're inside the castle walls.")
    direction = get_input('''Where do you want to go? Type "left" or "right"\n''')
    game_status = player_chooses("direction", direction)
    check_game_status(game_status)
    direction = get_input('''There is an undeground river in the castle, with a chamber at the other side? Type "wait" to wait for the boat, type "swim" to swim across.\n''')
    game_status = player_chooses("action", direction)
    check_game_status(game_status)
    direction = get_input('''You arrive at the chamber unharmed.  It has three doors. One red, one yellow and one blue, Which color do you choose?''')
    game_status = player_chooses("choose", direction)
    check_game_status(game_status)
    