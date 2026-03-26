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


# Main routine
print()
print("💿💿💿🖤 Welcome to the Higher Lower Game 🖤💿💿💿")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? 🤨 ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print()
print("Program continues")