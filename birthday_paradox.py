import datetime, random

# set up a tuple of month names in order
MONTHS = ("Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.",
          "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec.")

def intro():
    print("*" * 77)
    print("""\n Birthday paradox simulation: a probabilistic program.

            This paradox is about the 99.9 percent change of two people
                celebrating their birthday in the same day. Even is a small
                group of 23 people that probability if 50 percent.
                
            However, it is not actually a paradox, it\'s just a surprising
            result. 
""")
    print("*" * 77)

def get_birthdays(num_of_birthdays):
    """ return a list of number random date objects for birthdays"""
    birthdays = []
    for i in range(num_of_birthdays):
        # the year is important for the simulation as long as
        # all participants have been born in the same year
        start_year = datetime.date(2001, 1, 1)
        
        # get a random day into the year
        random_num_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_year + random_num_of_days
        birthdays.append(birthday)
        
    return birthdays

def get_match(birthdays, show=False):
    """ returns the date object of a birthday that occurs more than once
      in the birthday list. """
    if bool(show):
        print(" Birthdays list: ", birthdays)
        print("\n Birthdays set: ", set(birthdays))
        
    if len(birthdays) == len(set(birthdays)):
        return None # all birthdays are unique in this case
    
    # compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # returns the matching birthday

def generate_birthdays():
    # keep asking until the user enters a valid amount
    while True:
        print("\n\t How many birthdays shall I generate? (Max 100)")
        print("   >>>> Total of birthdays: ", end="")
        response = input()
        if response.isdecimal() and (0 < int(response) < 100):
            number_days = int(response)
            break # user has entered a valid amount
    print()
    # generate and display birthdays
    print("\n\t Here you are ", number_days, " birthdays:")
    birthdays = get_birthdays(number_days)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            # display a comma for each birthday after the first one
            print(", ", end="")
        month_name = MONTHS[birthday.month - 1]
        date_text = "{} {}".format(month_name, birthday.day)
        print(date_text, end="")
    print("\n\n")
    return number_days, birthdays

def find_matching_birthdays(dates_list):
    #determine if there are two birthdays that match
    date_match = get_match(dates_list, True)
    print("\n\t In this simulation, ", end="")
    if date_match != 0:
        month_name = MONTHS[date_match.month - 1]
        date_text = "{} {}".format(month_name, date_match.day)
        print("\n  >>> Multiple people have a birthday on ", date_text)
    else:
        print("\n\t There are no matching birthdays.\n")

def run_all_simulations(total_days):
    print("\n\t Generating ", total_days, " random birthdays 100,000 times...")
    input("\t Press Enter to begin...")
    
    print("\n\t Let us run another 100,000 simulations.\n")
    sim_match = 0 #how many simulations had matching birthdays in them
    for x in range(100_000):
        # report on the progress every 10,000 simulations
        if x % 10_000 == 0:
            print("  >>>> ", x, " simulations run so far...")
        birthdays = get_birthdays(total_days)
        if get_match(birthdays) != None:
            sim_match = sim_match + 1
    print("\n  :::::::: 100,000 simulations successfully run!")
    return sim_match

def display_sim_result(matches, days):
    probability = round(matches / 100000 * 100, 2)
    print("\n\t -----> Out of 100,000 simulations of ", days, " people there was ")
    print("\t          a matching birthday in that group ", matches, " times. This ")
    print("\t           means that ", days, " people have a ", probability, " % change of ")
    print("\t           having a matching birthday in their group.")

def start_app():
    intro()
    days, birthdays = generate_birthdays()
    find_matching_birthdays(birthdays)
    found_matches   = run_all_simulations(days)
    display_sim_result(found_matches, days)

if __name__ == '__main__':
    start_app()

