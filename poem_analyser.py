from time import sleep

#################################################################
# GLOBAL VARIABLES
#################################################################

VOWELS = 'AEIOUaeiou'
vowels_in_line = []
consonants_in_line = []
counter = 1
poem = []
#################################################################

#################################################################
# FUNCTIONS
#################################################################

def total_vowels(word):  
   vowel_list = [letter for letter in word if letter in VOWELS]
   return vowel_list

def total_consonants(word):
   cons_list = [letter for letter in word if letter not in VOWELS and letter.isalpha()]
   return cons_list

def adorn():
    sleep(0.2)
    print("**" * 28)
    sleep(0.2)
    print("\t   P O E M    A N A L Y Z E R  ")
    sleep(0.2)
    print("**" * 28)
    sleep(0.2)

def get_line_number():
    adorn()
    print("\n\tFor you to be able to type your poem,")
    sleep(0.4)
    try:
        total_lines = int(input("\tplease how many lines it will occupy: "))
    except ValueError:
        print("\t WARNING: The number of lines cannot be null or equal to zero!\n")
    finally:
        sleep(0.4)
        print("\n\tYou\'ve chosen a {} line limit.\n".format(total_lines))
    return total_lines

def save_poem(lines):
    global counter, poem
    while(counter <= lines):
        print("\t >>>> {} ".format(counter), end="")
        line = str(input())
        poem.append(line)
        line = " "
        counter += 1

    if (counter == lines+1):
        counter = 1
    return poem

def analyse_user_poem(poem):
    global vowels_in_line, consonants_in_line
    vowel_sum = 0
    cons_sum = 0
    cnt = 1
    print("\n\tThis is your poem:\n")
    print("\t")
    for line in poem:
        print("\t >>> " + str(cnt), end=" ")
        for word in line:
            vowels_in_line.extend(total_vowels(word))
            consonants_in_line.extend(total_consonants(word))
            print(word, end="")
            sleep(0.1)
        print("\n")
        sleep(0.2)
        print("\t ::: The number of vowels in this lines is: ", len(vowels_in_line))
        vowel_sum += len(vowels_in_line)
        vowels_in_line = []
        sleep(0.2)
        print("\t ::: The total of consonants is: ", len(consonants_in_line))
        cons_sum += len(consonants_in_line)
        consonants_in_line = []
        cnt += 1
        print("\n")
    return vowel_sum, cons_sum


def show_total(vowels, consonants):    
    sleep(0.3)
    print("\t\t ---> Total vowels in poem: {}.".format(vowels))
    sleep(0.3)
    print("\t\t  ---> Total consonants in poem: {}.\n".format(consonants))
    sleep(0.2)
    print("\n\n\t Thank you so much. GOODBYE!\n")
    adorn()

def run_app():
    num_of_lines = get_line_number()
    written_poem = save_poem(num_of_lines)
    vowels, consonants = analyse_user_poem(written_poem)
    show_total(vowels, consonants)

###############################################################
# Main routine
###############################################################
if __name__ == '__main__':
    try:
        run_app()

    except (KeyboardInterrupt, SystemExit):
        print(" User has stopped program execution. Goodbye!")
    
