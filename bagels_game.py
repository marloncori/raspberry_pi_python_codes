import random
from colors import *
from time import sleep

NUM_DIGITS  = 3 # Try setting it to 1 or 10
MAX_GUESSES = 10 # You can try and set it to 1 or 100

smile   = '\u1F60A'
confuse = '\u1F615'
sad     = '\u2639'

def get_secret_number():
    """ Returns a string made up of NUM_DIGITS unique random digits"""
    numbers = list("0123456789")
    random.shuffle(numbers) # shuffle them into a random order
    # get the list of NUM_DIGITS digits in the list for the secret number
    secret_num = ""
    for num in range(NUM_DIGITS):
        secret_num += str(numbers[num])
    return secret_num

def get_clues(guess, number):
    """ Returns a string message with pico, fermi, bagels clues for a guess"""
    msg = ""
    if guess == number:
        msg = "\t\t "+smile+" CONGRATULATIONS! You\'ve got it " + smile
        return msg
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == number[i]:
            # a corret digit in the right place
            clues.append(" >>"+cyan+"Fermi! "+e+smile)
        elif guess[i] in number:
            # a correct digit is the wrong place
            clues.append("  >>"+green+"Pico! "+e+confuse)
    if len(clues) == 0:
        msg = "\t\t>>"+red+"Bagels... "+e+sad
        return msg
    else:
        # sort the clues into alphabetical order so their original order
        # does not give information away :D
        clues.sort()
        # make a single string from the list of string clues
        msg = " ".join(clues)
        return msg
    
def intro():
    sleep(0.4)
    print("##" * 22)
    sleep(0.4)
    print("### "+cyan+"BAGELS"+e+": "+green+"a deductive logic game."+e+yellow+"\n\t Version by"+e+red+" Marlon Couto Ribeiro"+e+" ###")
    sleep(0.4)
    print("##" * 22)
    sleep(0.7)
    print("\n    I am thinking of  a"+cyan+" {}-digit number".format(NUM_DIGITS)+e, end=" ")
    sleep(0.7)
    print("with no repeated digits.")
    sleep(0.5)
    print("      Try to gues what it is. Here you are some "+purple+"CLUES:"+e)
    sleep(0.5)
    print("\n\t [When I say]   [It means...]\n\t   "+green+"Pico"+e+"          One digit is right, but in the wrong position.\n\t   "+cyan+"Fermi"+e+"         One digit is correct and in the right position.\n\t   "+red+"Bagels"+e+"        No digit is correct.\n")
    sleep(0.5)
    print("\n      For example, if the secret number was "+purple+"248"+e+" and your guess was "+red+"843,"+e)
    sleep(0.4)
    print("        the clues would have been "+cyan+"Fermi"+e+green+" Pico"+e+".\n")
    
def play():
    while True:
        # this stores the secret number the player needs to guess
        secret = get_secret_number()
        sleep(0.5)
        print("\n\t I\'ve thought of a number...")
        sleep(0.5)
        print("\t   and you\'ve got {} guess to get it right.\n".format(MAX_GUESSES))
        sleep(0.5)
        
        total_attempts = 1
        while total_attempts <= MAX_GUESSES:
            player_guess = ""
            while len(player_guess) != NUM_DIGITS or not player_guess.isdecimal():
                print("\t:::: Attempt # {}.".format(total_attempts))
                sleep(0.5)
                print("\t\t >>> Your guess: ", end="")
                player_guess = input()
                sleep(0.5)
                
            clues = get_clues(player_guess, secret)
            print(clues)
            total_attempts += 1
            
        # Ask player if they want to play again
        print("\n\t  Do you want to try again? (yes / no) Answer: ", end="")
        answer = input()
        if not answer.lower().startswith("y"):
            break
    print("\t\t  ---> Thanks for playing. Come back again!\n")
    sleep(0.4)
    print("##" * 22)
    sleep(0.4)
    print("### "+cyan+"BAGELS"+e+": "+green+"a deductive logic game."+e+yellow+"\n\t Version by"+e+red+" Marlon Couto Ribeiro"+e+" ###")
    sleep(0.4)
    print("##" * 22)


def start_game():
    intro()
    sleep(0.5)
    play()
    
if __name__ == '__main__':
    try:
        start_game()
    
    except (KeyboardInterrupt, SystemExit):
        print("   User has stopped program execution. Goodbye!")