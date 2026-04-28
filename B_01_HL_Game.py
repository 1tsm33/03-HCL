# checks users enter yes (y) or no (n)

def yes_no(question):

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("pleas enter yes / no")


def instructions():
    """Prints instructions"""

    print ("""
*** Instructions ***

To begin, choose the number of rounds and either customise 
the game parameters or go whith the default game (where the 
secret number will be at 1 too 100).

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to try to guess the secret number without
running out of guesses.

good luck, babe!

    """)

# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game

def int_check(question, low=None, high=None, exit_code=None):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infanite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks that the number is more than / equal to 1
            if response < 1:
                 print(error)
            else:
                return response

        except ValueError:
                 print(error)


# Main Routine Starts here

# Intialise game veriables
mode = "regular"
rounds_played = 0


print("💿💿💿🖤 Welcome to the Higher Lower Game 🖤💿💿💿")
print()

want_instructions = yes_no("Do you want to read the instructions? 🤨 ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ", low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Get Game parameters
low_num = int_check("Low Number? ")
high_num = int_check("High Number? ", low=low_num+1)
guesses_allowed = calc_guesses(low_num, high_num)
# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ Round {rounds_played + 1} (Infinite Mode) ♾♾♾"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # If user choice is exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
         num_rounds += 1



# Game Loop ends here

# Game Hisory / Statistics area